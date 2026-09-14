"""

Stooge sort takes a recursive approach that repeatedly sorts overlapping two-thirds portions of the collection, rather than splitting it into non-overlapping halves or thirds the way merge sort or quick sort do.

For a section of the collection containing two or more elements, the algorithm first compares the first and last elements of that section. If the first is larger than the last, they are swapped.

If the section contains three or more elements, three recursive steps are then performed: the first two-thirds of the section is sorted the same way, then the last two-thirds of the section is sorted the same way, and finally the first two-thirds is sorted one more time.

A section containing zero or one elements needs no work, since it is already sorted. This is the base case that stops the recursion.

Recursing on overlapping thirds

The reason the first two-thirds is sorted a third time, after the last two-thirds, is that sorting the last two-thirds can disturb elements that the first pass already placed correctly, since the two portions overlap in their middle third.

Sorting the first two-thirds again fixes any values that were pushed out of place by the second step, without disturbing the correct ordering that the last third of the section has by that point already achieved.

Because each recursive call only shrinks the section by one third at a time, and processes overlapping portions rather than disjoint ones, a very large number of comparisons end up being performed, far more than the other algorithms in this collection.

Example

Consider the sequence:

7, 3, 8, 2, 6

The first and last elements, 7 and 6, are compared. 7 is larger, so they are swapped:

6, 3, 8, 2, 7

The first two-thirds of the section, 6, 3, 8, 2, is sorted the same way, which produces 2, 3, 6, 8:

2, 3, 6, 8, 7

The last two-thirds of the section, 3, 6, 8, 7, is sorted the same way, which produces 3, 6, 7, 8:

2, 3, 6, 7, 8

The first two-thirds, 2, 3, 6, 7, is sorted one final time. It is already in order, so nothing changes:

2, 3, 6, 7, 8

The collection is now fully sorted.

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
