"""

Bogosort takes a very different approach from the other sorting algorithms in this collection: instead of methodically comparing and rearranging elements, it simply checks whether the collection happens to already be sorted, and if it is not, shuffles it into a completely new random order and checks again.

This is repeated, over and over, until a shuffle happens to land on a correctly sorted order purely by chance.

Checking and reshuffling

Checking whether a collection is sorted is straightforward: every adjacent pair of elements is compared, from the beginning to the end, and if any pair is found to be in the wrong order, the collection is not sorted.

If the check fails, the entire collection is randomly shuffled, with every possible arrangement equally likely, and the check is performed again.

There is no memory of previous attempts. Each shuffle is entirely independent of the ones before it, so a shuffle that was checked and rejected could, in principle, occur again later.

Because a shuffle produces a random arrangement out of every possible arrangement of the collection, and only one of those arrangements (or a small number, if there are duplicate values) is correctly sorted, the number of attempts needed grows extremely quickly as the collection gets larger. For even a modestly sized collection, this algorithm can be expected to take an impractically long time to finish.

Example

Consider the sequence:

7, 3, 8, 2, 6

This is checked and found not to be sorted, so it is shuffled. Suppose the result is:

3, 8, 7, 2, 6

This is also not sorted, so it is shuffled again. Suppose the result is:

2, 3, 6, 7, 8

This time, the check passes: every adjacent pair is in the correct order. The collection is sorted, and no further shuffles are needed.

In practice, landing on a correctly sorted order this quickly would be extremely lucky. For a collection of even a few dozen elements, an enormous number of shuffles would typically be needed before one happened to be sorted.

"""

import random # This sort uses random.shuffle(values), which randomly rearranges the elements in the list named values.



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
