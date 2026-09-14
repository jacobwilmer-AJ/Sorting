"""

Counting sort works differently from the sorting algorithms that compare elements against each other. Instead, it counts how many times each value appears in the collection, and uses those counts to figure out exactly where every element belongs in the final sorted result.

This approach only works when the values are non-negative integers within a range that is not too large, since the algorithm needs to keep a count for every possible value in that range.

Counting occurrences

The algorithm first finds the largest value in the collection, so it knows how many counts it needs to keep track of.

It then creates a list of counts, one for every possible value from zero up to that largest value, all starting at zero.

It scans the original collection once, and for every value encountered, increases the count at that value's position by one.

At this point, the count at each position tells you how many times that exact value appeared in the collection.

Placing values into position

To turn these counts into actual positions in the sorted result, the algorithm adds each count to the sum of all the counts before it. This is called a running, or prefix, sum.

After this step, the count stored at a given value no longer means "how many times did this value appear." Instead, it means "how many values in the final sorted result are less than or equal to this value," which is exactly the position (plus one) where the last occurrence of that value belongs.

The algorithm then scans the original collection one more time, from the end toward the beginning. For each value, it looks up the running count for that value, places the value at that position (minus one) in the output, and decreases the running count by one so that an earlier occurrence of the same value will be placed just before it.

Scanning from the end toward the beginning, rather than the other way around, is what keeps equal values in their original relative order.

Example

Consider the sequence:

7, 3, 8, 2, 6

The largest value is 8, so counts are kept for every value from 0 to 8.

After scanning the collection once, the counts are:

value:  0  1  2  3  4  5  6  7  8
count:  0  0  1  1  0  0  1  1  1

Turning these into running sums produces:

value:  0  1  2  3  4  5  6  7  8
count:  0  0  1  2  2  2  3  4  5

The collection is then scanned from the end toward the beginning: 6, 2, 8, 3, 7.

6 has a running count of 3, so it is placed at position 2, and its count becomes 2.

2 has a running count of 1, so it is placed at position 0, and its count becomes 0.

8 has a running count of 5, so it is placed at position 4, and its count becomes 4.

3 has a running count of 2, so it is placed at position 1, and its count becomes 1.

7 has a running count of 4, so it is placed at position 3, and its count becomes 3.

The resulting output, read from position 0 to 4, is:

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
