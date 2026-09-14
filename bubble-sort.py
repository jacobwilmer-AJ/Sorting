
"""

Bubble sort divides the collection conceptually into two sections:

A section at the beginning containing the elements that are still
being sorted.

A section at the end containing elements that have already been
placed into their final positions.

Initially, the entire collection is considered unsorted.

The algorithm then makes a pass through the collection, comparing
each pair of adjacent elements.

For each pair of adjacent elements, there are two possibilities.

If the element on the left is smaller than or equal to the element
on the right, the two elements are already in the correct relative
order, so nothing needs to be done.

If the element on the left is larger than the element on the right,
the two elements are in the wrong order and must be swapped.

This process continues from the beginning of the collection toward
the end.

When the end of the unsorted portion is reached, the largest element
in that portion will have moved all the way to the end. This element
is now in its final position and does not need to be considered in
future passes.

The algorithm then begins another pass, but this time it can ignore
the element that was just placed at the end.

After every pass, one additional element is therefore known to be
in its final position.

The process continues until the entire collection is sorted.


Making a pass

A pass begins at the first element of the unsorted portion.

The algorithm compares the first element with the element immediately
after it.

If the first element is larger, the two elements are swapped.

The algorithm then moves one position to the right and compares the
next pair of adjacent elements.

Importantly, the algorithm does not restart from the beginning after
each comparison. It continues moving toward the end, examining each
adjacent pair in sequence.

Because a larger element can be swapped repeatedly as it encounters
smaller elements, a large value can move many positions toward the
end during a single pass.

If an entire pass completes without any swaps, every adjacent pair
was already in the correct order, meaning the collection is already
sorted. The algorithm can stop immediately rather than performing
any additional passes.


Example

Consider the sequence:

7, 3, 8, 2, 6

Initially, the entire collection is unsorted:

7, 3, 8, 2, 6

The first pass begins by comparing 7 and 3. Since 7 is larger, they
are swapped:

3, 7, 8, 2, 6

The algorithm then compares 7 and 8. They are already in the correct
order, so nothing changes:

3, 7, 8, 2, 6

The algorithm then compares 8 and 2. Since 8 is larger, they are
swapped:

3, 7, 2, 8, 6

Finally, 8 and 6 are compared. Since 8 is larger, they are swapped:

3, 7, 2, 6, 8

The first pass is complete.

The largest element, 8, is now at the end of the collection and
will not need to be examined again:

3, 7, 2, 6 | 8

The second pass therefore only considers the first four elements.

The algorithm compares 3 and 7. They are already in the correct
order:

3, 7, 2, 6 | 8

It then compares 7 and 2. Since 7 is larger, they are swapped:

3, 2, 7, 6 | 8

It then compares 7 and 6. Since 7 is larger, they are swapped:

3, 2, 6, 7 | 8

The second pass is complete.

The two largest elements are now in their final positions:

3, 2, 6 | 7, 8

The third pass considers only the first three elements.

3 and 2 are compared. Since 3 is larger, they are swapped:

2, 3, 6 | 7, 8

The algorithm then compares 3 and 6. They are already in the
correct order:

2, 3, 6 | 7, 8

The third pass is complete.

The collection is now:

2, 3, 6 | 7, 8

The fourth pass examines the remaining unsorted portion.

2 and 3 are already in the correct order, and 3 and 6 are also
already in the correct order.

No swaps are necessary.

At this point the collection is completely sorted:

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
