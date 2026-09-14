"""

Merge sort works by dividing the collection in half, recursively sorting each half, and then merging the two sorted halves back together into a single sorted collection.

A collection containing zero or one elements is already sorted, since there is nothing to compare it against. This is the base case that stops the recursion.

For a larger collection, the algorithm splits it into a left half and a right half at the midpoint.

Each half is sorted using the same process: split it further, sort the smaller pieces, and merge them back together.

Once both halves have been fully sorted, they are combined using a merge step.

Merging two sorted halves

To merge two sorted halves into one sorted collection, the algorithm looks at the front of each half.

Whichever front element is smaller is removed from its half and appended to the result.

This comparison and removal repeats, always comparing the current front of each half, until one of the halves has been completely emptied.

Once a half is empty, there is nothing left to compare against, so every remaining element in the other half is appended to the result in order.

Because both halves were already sorted before merging began, the result of this process is a single fully sorted collection.

Example

Consider the sequence:

7, 3, 8, 2, 6

The collection is split into two halves:

7, 3 | 8, 2, 6

Each half is sorted the same way, by splitting it further and merging the pieces back together. Sorting 7, 3 produces 3, 7. Sorting 8, 2, 6 produces 2, 6, 8.

The two sorted halves, 3, 7 and 2, 6, 8, are then merged.

The fronts of each half, 3 and 2, are compared. 2 is smaller, so it is taken first:

Result: 2
Remaining: 3, 7 | 6, 8

The fronts, 3 and 6, are compared. 3 is smaller:

Result: 2, 3
Remaining: 7 | 6, 8

The fronts, 7 and 6, are compared. 6 is smaller:

Result: 2, 3, 6
Remaining: 7 | 8

The fronts, 7 and 8, are compared. 7 is smaller:

Result: 2, 3, 6, 7
Remaining: (empty) | 8

The left half is now empty, so the rest of the right half is appended directly:

Result: 2, 3, 6, 7, 8

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
