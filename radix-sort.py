"""

Radix sort works by sorting a collection of non-negative integers one digit at a time, starting from the ones digit and moving toward the most significant digit.

Each pass sorts the entire collection by a single digit, using counting sort as the method for that pass, since counting sort naturally works on a small range of possible digits: 0 through 9.

The key property that makes this work is that counting sort is stable: it never changes the relative order of elements that have equal values in the digit being examined. Because of this, elements that were already placed correctly by an earlier, less significant digit stay in that relative order during later passes, unless the new digit says otherwise.

After sorting by the ones digit, then the tens digit, then the hundreds digit, and so on, the entire collection ends up fully sorted once every digit position up to the largest number's most significant digit has been processed.

Sorting by one digit

For a given digit position, the algorithm extracts that digit from every value: dividing by the place value (1 for ones, 10 for tens, 100 for hundreds, and so on) and taking the remainder after dividing by 10.

It then performs a counting sort using these extracted digits, in exactly the same way ordinary counting sort works: counting how many times each digit (0 through 9) occurs, turning those counts into running sums, and placing each original value into the output based on its digit's running count, scanning from the end of the collection to keep equal digits in their original relative order.

Once every value has been placed based on this digit, the pass is complete, and the next, more significant digit is processed the same way.

Example

This example uses two-digit numbers, since single-digit numbers would only need one pass to demonstrate the process.

Consider the sequence:

72, 38, 15, 60, 24

The largest value is 72, which has two digits, so two passes are needed: one for the ones digit, one for the tens digit.

The ones digits are: 2, 8, 5, 0, 4. Sorting by these digits produces:

60, 72, 24, 15, 38

The tens digits of this new arrangement are: 6, 7, 2, 1, 3. Sorting by these digits produces:

15, 24, 38, 60, 72

The largest value, 72, has no hundreds digit, so no further passes are needed. The collection is now fully sorted:

15, 24, 38, 60, 72

"""


def sort(values):
    pass


if __name__ == "__main__":
    import random
    import time

    # Set the list of values using one of the following, and leave the other commented out:
    # Generate a list of 10 random integers between 1 and 100.
    length = 20
    values = [random.randint(1, 100) for _ in range(length)]

    # or set the list of values yourself to whatever you wish.
    # values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print("Unsorted:", values)

    start_time = time.time()
    result = sort(values)
    end_time = time.time()

    # Some sort() functions sort in place and return None; others
    # return a new sorted list. This works either way.
    if result is not None:
        values = result

    print("Sorted:", values)
    print(f"Sorting took {end_time - start_time:.6f} seconds.")
