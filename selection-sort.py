"""

Selection sort divides the collection conceptually into two sections:

A sorted section, which begins at the first position.
An unsorted section, containing everything after it.

Initially, the sorted section is empty and the entire collection is unsorted.

The algorithm repeatedly finds the smallest value in the unsorted section and moves it to the front of that section, directly after the sorted section.

Once that value has been moved, the sorted section grows by one element and the unsorted section shrinks by one element.

This continues until the unsorted section is empty and the entire collection has been placed in order.

Finding the minimum

To find the smallest value in the unsorted section, the algorithm keeps track of the index of the smallest value seen so far, starting with the first element of the unsorted section.

It then examines each remaining element in the unsorted section in turn, comparing it with the current smallest value found.

Whenever a smaller value is found, that element's index becomes the new smallest-value index.

After every element in the unsorted section has been examined, the tracked index points to the overall smallest value.

That value is then swapped into the first position of the unsorted section, placing it at the boundary between the sorted and unsorted sections.

If the smallest value was already in that first position, no swap is necessary.

Example

Consider the sequence:

7, 3, 8, 2, 6

Initially, nothing is sorted:

| 7, 3, 8, 2, 6

The unsorted section is scanned for its smallest value. 7 is compared with 3, which is smaller. 3 is compared with 8, which is not smaller. 3 is compared with 2, which is smaller. 3 is compared with 6, which is not smaller. The smallest value found is 2.

2 is swapped with the first element of the unsorted section, 7:

2 | 3, 8, 7, 6

The unsorted section is scanned again. 3 is the smallest value found, and it is already in the first position, so no swap is needed:

2, 3 | 8, 7, 6

The unsorted section is scanned again. 8 is compared with 7, which is smaller. 7 is compared with 6, which is smaller. The smallest value found is 6, so it is swapped with the first element of the unsorted section, 8:

2, 3, 6 | 7, 8

The unsorted section is scanned one last time. 7 is compared with 8, which is not smaller. 7 is already in the first position, so no swap is needed:

2, 3, 6, 7 | 8

Only one element remains, so it is already in its final position:

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
