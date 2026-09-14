"""

Heap sort works by first rearranging the collection into a max-heap, and then repeatedly removing the largest remaining element and placing it at the end of the collection.

A max-heap is an arrangement of elements, stored directly in the list, where every element is greater than or equal to its children. If an element is at index i, its children are located at indices 2i + 1 and 2i + 2.

Because the largest element of a max-heap is always at the very front, index 0, that element can be found immediately without searching.

Building the initial heap

The algorithm converts the collection into a max-heap by processing every element that has at least one child, starting from the last such element and working backward to the front of the collection.

For each of these elements, a sift down operation is performed to make sure the max-heap property holds at that position.

Sifting a node down

To sift a node down, the algorithm compares it with its two children (skipping any child that does not exist).

If the node is already greater than or equal to both children, nothing needs to change, since the max-heap property already holds there.

If one of the children is larger, the node is swapped with the larger of the two children. The node has now moved one level down the tree, so the same comparison is repeated at its new position.

This continues until the node is greater than or equal to both of its children, or until it has no children left to compare against.

Removing the largest element

Once the max-heap has been built, the largest element is at the front of the collection.

That element is swapped with the last element of the remaining heap, which places the largest value into its final sorted position at the end.

The heap is then considered one element smaller, and a sift down is performed on the new front element to restore the max-heap property.

This process, removing the front and sifting down, repeats until only one element remains in the heap, at which point the entire collection is sorted.

Example

Consider the sequence:

7, 3, 8, 2, 6

Building the heap starts at the last element with children, index 1 (value 3), whose children are 2 (index 3) and 6 (index 4). Since 6 is the largest of the three, 3 is swapped with 6:

7, 6, 8, 2, 3

Next, index 0 (value 7) is processed. Its children are 6 (index 1) and 8 (index 2). Since 8 is the largest of the three, 7 is swapped with 8:

8, 6, 7, 2, 3

7 is then compared with its children, at indices 5 and 6, which do not exist, so no further swap is needed. The collection is now a valid max-heap.

The largest element, 8, is swapped with the last element of the heap, 3:

3, 6, 7, 2, 8

The heap is now considered to end at index 3. 3 is sifted down: its children are 6 and 7, so it is swapped with the larger, 7:

7, 6, 3, 2, 8

The next largest element, 7, is swapped with the last element of the remaining heap, 2:

2, 6, 3, 7, 8

The heap is now considered to end at index 2. 2 is sifted down: its children are 6 and 3, so it is swapped with the larger, 6:

6, 2, 3, 7, 8

6 is swapped with the last element of the remaining heap, 3:

3, 2, 6, 7, 8

The heap is now considered to end at index 1. 3 is sifted down: its only child is 2, which is not larger, so no swap is needed.

3 is swapped with the last element of the remaining heap, 2:

2, 3, 6, 7, 8

Only one element remains in the heap, so the collection is now fully sorted:

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
