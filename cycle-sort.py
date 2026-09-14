"""

Cycle sort works by placing every element directly into its final sorted position, one at a time, using as few writes to the collection as possible. Most other sorting algorithms move an element several times before it reaches its final position; cycle sort moves each element at most once.

The algorithm processes one starting position at a time, from the beginning of the collection to the second-to-last position.

Finding an element's final position

For the element currently at the starting position, the algorithm counts how many elements elsewhere in the collection are smaller than it. That count is exactly how many positions ahead of the starting position this element's correct, final position is.

If that final position turns out to be the same as the starting position, the element is already correctly placed, and nothing more needs to be done for it.

Otherwise, the element that currently occupies that final position needs to move somewhere else before the current element can be placed there. The current element is swapped into its final position, and the element that used to be there becomes the new element being placed.

This new element then goes through the same process: counting how many elements are smaller than it to find its own final position, and swapping into that position. If an equal value is already sitting at the destination, the algorithm skips past it to the next position, so that equal values do not endlessly swap with each other.

This chain of swaps, called a cycle, continues until an element is placed back at the original starting position, closing the cycle. Because every swap in a cycle places one element directly into its final position, a cycle of length k is completed using only k writes to the collection.

Example

Consider the sequence:

7, 3, 8, 2, 6

Starting at position 0, the value is 7. Three elements (3, 2, 6) are smaller than 7, so its final position is index 3. The element there, 2, is displaced, and 7 is written into position 3:

7, 3, 8, 7, 6

2, the displaced value, is now placed: no elements are smaller than 2, so its final position is index 0, the position where this cycle began. 2 is written there, closing the cycle:

2, 3, 8, 7, 6

Starting at position 1, the value is 3. No elements after it are smaller, so its final position is index 1, where it already is. Nothing more is done.

Starting at position 2, the value is 8. Two elements (7, 6) are smaller than 8, so its final position is index 4. The element there, 6, is displaced, and 8 is written into position 4:

2, 3, 8, 7, 8

6, the displaced value, is now placed: no remaining elements are smaller than it, so its final position is index 2, where this cycle began. 6 is written there, closing the cycle:

2, 3, 6, 7, 8

Starting at position 3, the value is 7. No elements after it are smaller, so its final position is index 3, where it already is. Nothing more is done.

The collection is now fully sorted, and only four writes were needed to move the elements that were out of place:

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
