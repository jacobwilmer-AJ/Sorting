
import importlib.util
import random
import threading
import time
from pathlib import Path


# Sizes to test, from smallest to largest.
TEST_SIZES = [10, 100, 1_000]

# Maximum number of seconds a single sort is given to finish.
TIMEOUT_SECONDS = 10.0

# Files named "answer-<something>-sort.py" hold reference solutions
# for exercises where <something>-sort.py has been left for a student
# to fill in. Normally they're excluded from the benchmark run; set
# this to True to run only those answer files instead.
RUN_ANSWERS = False

# Directory containing this file and the sorting implementations.
SORTING_DIRECTORY = Path(__file__).parent

# Prefix that marks a file as an answer file rather than a student's
# own attempt.
ANSWER_PREFIX = "answer-"


class Counter:
    """
    Tracks how many element comparisons a sorting algorithm performs.
    """

    def __init__(self):
        self.comparisons = 0


class CountingValue:
    """
    Wraps a single value so that comparing it against another
    CountingValue increments a shared Counter.

    A sort() implementation never sees this class or the counter.
    It just compares list elements the normal way, e.g.

        if values[i] > values[i + 1]:

    Because values[i] is a CountingValue, that ">" calls
    CountingValue.__gt__ below, which records the comparison and
    then delegates to the wrapped value. This lets main.py measure
    comparisons for any student-written sort.py without requiring
    any changes to that file.
    """

    __slots__ = ("value", "counter")

    def __init__(self, value, counter):
        self.value = value
        self.counter = counter

    def _unwrap(self, other):
        self.counter.comparisons += 1
        return other.value if isinstance(other, CountingValue) else other

    def __lt__(self, other):
        return self.value < self._unwrap(other)

    def __le__(self, other):
        return self.value <= self._unwrap(other)

    def __gt__(self, other):
        return self.value > self._unwrap(other)

    def __ge__(self, other):
        return self.value >= self._unwrap(other)

    def __eq__(self, other):
        return self.value == self._unwrap(other)

    def __ne__(self, other):
        return self.value != self._unwrap(other)

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return repr(self.value)

    # These do not count as comparisons. They exist so that
    # non-comparison-based sorts (counting sort, radix sort, bucket
    # sort) can use a value as a list index or convert it with int(),
    # exactly as they would with a plain integer.
    def __index__(self):
        return self.value

    def __int__(self):
        return int(self.value)


def load_sort_algorithms(run_answers=False):
    """
    Find every Python file ending in '-sort.py' and import it.

    Each sorting file is expected to contain a function:

        sort(values)

    The function should sort the supplied list and either:
      - return the sorted list, or
      - sort the list in-place and return None.

    By default, files whose name starts with "answer-" are skipped,
    since those hold reference solutions rather than a student's own
    attempt. Pass run_answers=True (see the RUN_ANSWERS constant
    above) to load only those answer files instead.
    """

    algorithms = []

    for file_path in sorted(SORTING_DIRECTORY.glob("*-sort.py")):
        is_answer_file = file_path.stem.startswith(ANSWER_PREFIX)

        if is_answer_file != run_answers:
            continue

        module_name = file_path.stem.replace("-", "_")

        spec = importlib.util.spec_from_file_location(
            module_name,
            file_path
        )

        if spec is None or spec.loader is None:
            print(f"Could not load {file_path.name}")
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "sort"):
            print(f"Skipping {file_path.name}: no sort() function found")
            continue

        # Drop the "answer-" prefix so answer runs display under the
        # same name as the exercise they're the solution to.
        name = file_path.stem
        if is_answer_file:
            name = name[len(ANSWER_PREFIX):]

        algorithms.append({
            "name": name,
            "module": module,
            "sort": module.sort
        })

    return algorithms


def build_test_cases():
    """
    Build one random test case for each requested size.

    A separate list is generated for every size so that every
    sorting algorithm receives exactly the same data for that size.
    """

    test_cases = {}

    for size in TEST_SIZES:
        values = list(range(size))
        random.shuffle(values)
        test_cases[size] = values

    return test_cases


def run_sort(sort_function, original_values):
    """
    Run a sorting algorithm on a copy of the test data, giving it at
    most TIMEOUT_SECONDS to finish.

    The sort runs on a background thread so that a sort which never
    finishes (an infinite loop, or simply one that is astronomically
    slow, such as bogosort on a large list) does not stop the rest of
    the benchmark from running. Python cannot forcibly kill a thread,
    so a timed-out sort is left running in the background as a daemon
    thread; it will not block the program from exiting.

    Returns:
        elapsed_time: seconds elapsed before finishing or timing out
        comparisons: number of element comparisons made so far
        status: "YES", "NO", or "TIMED OUT"
    """

    counter = Counter()
    values = [CountingValue(value, counter) for value in original_values]

    outcome = {}

    def target():
        try:
            outcome["result"] = sort_function(values)
        except Exception as error:
            outcome["error"] = error

    start_time = time.perf_counter()

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(TIMEOUT_SECONDS)

    elapsed_time = time.perf_counter() - start_time

    if thread.is_alive():
        return elapsed_time, counter.comparisons, "TIMED OUT"

    if "error" in outcome:
        raise outcome["error"]

    result = outcome.get("result")

    # Support both common sorting styles:
    #
    # 1. sort(values) modifies the list in-place and returns None.
    # 2. sort(values) returns a new sorted list.
    if result is None:
        sorted_values = values
    else:
        sorted_values = result

    # Unwrap the CountingValues back into plain values for comparison
    # against the expected result.
    unwrapped_values = [value.value for value in sorted_values]

    correctly_sorted = (
        unwrapped_values == sorted(original_values)
    )

    status = "YES" if correctly_sorted else "NO"

    return elapsed_time, counter.comparisons, status


NAME_WIDTH = 25
TIME_WIDTH = 16
COMPARISONS_WIDTH = 15
CORRECT_WIDTH = 15


def overall_status(runs):
    """
    Collapse a list of per-size run statuses into a single status
    for the whole algorithm.

    A single incorrect result is worse than a timeout, and a timeout
    is worse than every run succeeding, so the worst status found is
    the one reported.
    """

    statuses = [run["status"] for run in runs]

    if "NO" in statuses:
        return "NO"

    if "TIMED OUT" in statuses:
        return "TIMED OUT"

    return "YES"


def print_results(results, sizes):
    """
    Print all results as a formatted table, one row per algorithm.

    Each size being tested contributes its own Time and Comparisons
    columns, so the table automatically grows or shrinks to match
    however many sizes are in `sizes`. A single Correct column at the
    end summarizes every run for that algorithm.
    """

    group_width = TIME_WIDTH + COMPARISONS_WIDTH
    total_width = NAME_WIDTH + group_width * len(sizes) + CORRECT_WIDTH

    print()
    print("=" * total_width)
    print("SORTING ALGORITHM BENCHMARK")
    print("=" * total_width)
    print()

    # Top header row: one label per size, spanning that size's two
    # columns (Time and Comparisons).
    top_header = f"{'':<{NAME_WIDTH}}"
    for size in sizes:
        top_header += f"{'n = ' + format(size, ','):^{group_width}}"
    top_header += f"{'':>{CORRECT_WIDTH}}"
    print(top_header)

    # Bottom header row: the actual column names.
    bottom_header = f"{'Algorithm':<{NAME_WIDTH}}"
    for _ in sizes:
        bottom_header += f"{'Time (s)':>{TIME_WIDTH}}"
        bottom_header += f"{'Comparisons':>{COMPARISONS_WIDTH}}"
    bottom_header += f"{'Correct':>{CORRECT_WIDTH}}"
    print(bottom_header)

    print("-" * total_width)

    for result in results:
        row = f"{result['algorithm']:<{NAME_WIDTH}}"

        for run in result["runs"]:
            row += f"{run['time']:>{TIME_WIDTH}.6f}"
            row += f"{run['comparisons']:>{COMPARISONS_WIDTH},}"

        row += f"{result['correct']:>{CORRECT_WIDTH}}"

        print(row)

    print("=" * total_width)


def main():
    if RUN_ANSWERS:
        print("Loading answer sorting algorithms...")
    else:
        print("Loading sorting algorithms...")

    algorithms = load_sort_algorithms(run_answers=RUN_ANSWERS)

    if not algorithms:
        if RUN_ANSWERS:
            print("No 'answer-*-sort.py' files containing a sort() function were found.")
        else:
            print("No '*-sort.py' files containing a sort() function were found.")
        return

    print(f"Found {len(algorithms)} sorting algorithm(s):")

    for algorithm in algorithms:
        print(f"  - {algorithm['name']}")

    print()

    print("Building test cases...")
    test_cases = build_test_cases()

    results = []

    for algorithm in algorithms:
        print(f"\nRunning {algorithm['name']}...")

        runs = []

        for size in TEST_SIZES:
            print(
                f"  Testing {size:,} elements...",
                end=" ",
                flush=True
            )

            try:
                elapsed_time, comparisons, status = run_sort(
                    algorithm["sort"],
                    test_cases[size]
                )

                runs.append({
                    "size": size,
                    "time": elapsed_time,
                    "comparisons": comparisons,
                    "status": status
                })

                print(
                    f"{elapsed_time:.6f} seconds, "
                    f"{comparisons:,} comparisons "
                    f"[Correct: {status}]"
                )

            except Exception as error:
                print(f"FAILED: {error}")

                runs.append({
                    "size": size,
                    "time": float("nan"),
                    "comparisons": 0,
                    "status": "NO"
                })

        results.append({
            "algorithm": algorithm["name"],
            "runs": runs,
            "correct": overall_status(runs)
        })

    print_results(results, TEST_SIZES)


if __name__ == "__main__":
    main()

