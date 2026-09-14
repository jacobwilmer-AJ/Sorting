"""

Gnome sort works similarly to insertion sort, in that it builds up a sorted section at the front of the collection, but it does so using a single position that moves back and forth, one step at a time, rather than shifting a whole group of elements at once.

The algorithm keeps track of one position in the collection. Whenever the element at that position is in the correct order relative to the element immediately before it, the position moves forward by one.

Whenever those two elements are in the wrong order, they are swapped, and the position moves backward by one instead of forward.

Moving backward after a swap allows the algorithm to check whether the element that was just moved earlier is also out of order with whatever now precedes it, in the same way that insertion sort keeps shifting a value backward until it finds its correct place.

Stepping forward and back

If the position is at the very beginning of the collection, there is nothing before it to compare against, so the position simply moves forward.

Otherwise, the element at the position is compared with the element immediately before it.

If the earlier element is smaller than or equal to it, the two elements are already in the correct order, and the position moves forward by one, extending the sorted section by one element.

If the earlier element is larger, the two elements are swapped, which fixes their relative order but may have introduced a new problem with whatever comes before the earlier element. The position moves backward by one so that pair can be checked next.

This continues, moving forward through elements that are already in order and backward whenever a swap is needed, until the position reaches the end of the collection.

Example

Consider the sequence:

7, 3, 8, 2, 6

The position starts at the beginning, so it moves forward with no comparison.

At position 1, 7 and 3 are compared. 7 is larger, so they are swapped and the position moves back:

3, 7, 8, 2, 6

At position 0, there is nothing before it, so the position moves forward again, and then forward again through position 1 and position 2, since 3 and 7, then 7 and 8, are already in order.

At position 3, 8 and 2 are compared. 8 is larger, so they are swapped and the position moves back:

3, 7, 2, 8, 6

At position 2, 7 and 2 are compared. 7 is larger, so they are swapped and the position moves back:

3, 2, 7, 8, 6

At position 1, 3 and 2 are compared. 3 is larger, so they are swapped and the position moves back:

2, 3, 7, 8, 6

The position then moves forward from the beginning through position 1 and position 2, since 2 and 3, then 3 and 7, are already in order.

At position 3, 7 and 8 are compared. They are in order, so the position moves forward.

At position 4, 8 and 6 are compared. 8 is larger, so they are swapped and the position moves back:

2, 3, 7, 6, 8

At position 3, 7 and 6 are compared. 7 is larger, so they are swapped and the position moves back:

2, 3, 6, 7, 8

The position then steps forward through the rest of the collection, finding every remaining pair already in order, until it reaches the end.

The collection is now fully sorted:

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
