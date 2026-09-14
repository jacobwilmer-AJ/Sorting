# Sorting Algorithms Practice

This folder has one file per classic sorting algorithm, each with the explanation written in but the actual code left for you to write, plus a benchmark tool (`main.py`) that automatically tests, times, and checks whatever you write.

## 1. Setup

You need Python 3 installed. Check with:

```bash
python --version
```

(On Mac/Linux this might be `python3 --version` instead.) Anything Python 3.8 or newer is fine. There's nothing else to install — everything here is plain Python, no external packages.

## 2. How each file is organized

Every `<name>-sort.py` file (e.g. `bubble-sort.py`) has three parts, in this order:

1. **A docstring at the top** — explains how the algorithm works conceptually, plus a worked example tracing through the sequence `7, 3, 8, 2, 6` step by step.
2. **A `sort(values)` function** — currently just:
   ```python
   def sort(values):
       pass
   ```
   This is the part you write.
3. **A `if __name__ == "__main__":` block at the bottom** — lets you run the file by itself to try your implementation out directly.

## 3. Your task

For each algorithm:

1. Read the docstring at the top of the file — it explains the idea and walks through an example by hand.
2. Implement `sort(values)`. You can do this either way:
   - Sort the list **in place** (modify `values` directly, `return` nothing), or
   - Build and `return` a **brand-new sorted list**, leaving the original untouched.

   Both styles are used across this collection already — pick whichever fits the algorithm better. The benchmark tool handles either one automatically.
3. Test it (see below), fix anything that's wrong, repeat.

## 4. Testing your implementation

There are two ways to try your code out.

### Option 1 — run one file by itself

```bash
python bubble-sort.py
```

This builds a random list of 20 numbers, runs it through your `sort()`, and prints the list before and after, along with how long it took.

To test specific numbers instead of random ones, open the file, find this part near the bottom, and switch which line is commented out:

```python
# Set the list of values using one of the following, and leave the other commented out:
# Generate a list of 10 random integers between 1 and 100.
length = 20
values = [random.randint(1, 100) for _ in range(length)]

# or set the list of values yourself to whatever you wish.
# values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Option 2 — run the full benchmark

```bash
python main.py
```

This automatically finds every `<name>-sort.py` file in the folder, runs each one's `sort()` against several lists of increasing size, and prints a results table. For each size it shows:

- **Time (s)** — how long that run took
- **Comparisons** — how many times your code compared two elements against each other. You don't need to do anything special for this to work — it's tracked automatically behind the scenes, no matter how you write your comparisons (`<`, `>`, `==`, etc.).

The **Correct** column on the far right sums up every size in one word:

| Value | Meaning |
|---|---|
| `YES` | Every size sorted correctly |
| `NO` | At least one size came out wrong — or `sort()` isn't implemented yet |
| `TIMED OUT` | At least one size didn't finish within the time limit |

Until you fill in a `sort()` function, it'll show up as `NO` with `0` comparisons — that's expected, not an error.

## 5. Algorithms in this folder

Roughly in a sensible order to tackle them:

1. `bubble-sort.py`
2. `insertion-sort.py`
3. `selection-sort.py`
4. `gnome-sort.py`
5. `merge-sort.py`
6. `quick-sort.py`
7. `heap-sort.py`
8. `counting-sort.py`
9. `radix-sort.py`
10. `bucket-sort.py`
11. `tree-sort.py`
12. `cycle-sort.py`
13. `stooge-sort.py`
14. `bogo-sort.py`

## 6. A couple of things worth knowing

- **You never need to count comparisons yourself.** Just write normal comparisons in your code — the benchmark counts them for you.
- **`bogo-sort.py` and `stooge-sort.py` are supposed to be slow.** Don't be surprised if they show `TIMED OUT` for larger sizes even with a correct implementation — that's the whole point of those two.
- **You shouldn't need to edit `main.py`.** It's the shared driver that discovers and runs every sort file automatically.
