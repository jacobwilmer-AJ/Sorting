"""

Quick sort works by choosing one element from the collection, called the pivot, and rearranging the collection so that every element smaller than or equal to the pivot comes before it, and every element greater than the pivot comes after it.

This rearrangement is called partitioning. Once it is complete, the pivot is in its final sorted position, because every element that needs to be to its left is to its left, and every element that needs to be to its right is to its right.

The elements before the pivot and the elements after the pivot are not yet sorted relative to each other. Each of those two sections is then partitioned the same way, recursively, using the same process.

A section containing zero or one elements needs no further work, since it is already sorted. This is the base case that stops the recursion.

Partitioning around a pivot

This implementation always chooses the last element of the section as the pivot.

A boundary index is maintained, starting just before the beginning of the section. This boundary marks the end of the elements confirmed to belong before the pivot.

The algorithm then scans every other element in the section, from the beginning up to (but not including) the pivot.

Whenever an element smaller than or equal to the pivot is found, the boundary is advanced by one position, and the element at the new boundary is swapped with the element that was found.

After the entire section has been scanned, everything up to the boundary is smaller than or equal to the pivot. The pivot is then swapped into the position immediately after the boundary, placing it correctly between the smaller and larger elements.

Example

Consider the sequence:

7, 3, 8, 2, 6

The pivot is the last element, 6. The boundary starts before the section, at index -1.

7 is compared with the pivot, 6. 7 is not smaller than or equal to 6, so it is skipped.

3 is compared with the pivot. 3 is smaller than or equal to 6, so the boundary advances to index 0, and 3 is swapped into that position:

3, 7, 8, 2, 6

8 is compared with the pivot. 8 is not smaller than or equal to 6, so it is skipped.

2 is compared with the pivot. 2 is smaller than or equal to 6, so the boundary advances to index 1, and 2 is swapped into that position:

3, 2, 8, 7, 6

Every element before the pivot has now been examined. The pivot is swapped into the position immediately after the boundary, index 2:

3, 2, 6, 7, 8

The pivot, 6, is now in its final position, with 3, 2 before it and 7, 8 after it.

Each of those two sections is partitioned the same way. Partitioning 3, 2 around the pivot 2 produces 2, 3. Partitioning 7, 8 around the pivot 8 leaves it unchanged, since 7 is already smaller than the pivot.

The final result is:

2, 3, 6, 7, 8

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
