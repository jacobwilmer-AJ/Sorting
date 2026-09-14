"""

Bucket sort works by dividing the range of possible values into several smaller ranges, called buckets, placing every element into the bucket that matches its value, sorting each bucket individually, and then combining the buckets back together in order.

Because each bucket only needs to hold a small portion of the collection, sorting an individual bucket is fast, even using a simple algorithm. Once every bucket has been sorted, concatenating them in order produces the full sorted collection, since every value in an earlier bucket is guaranteed to be smaller than every value in a later bucket.

This works best when the values are spread out fairly evenly across their range, so that no single bucket ends up holding a disproportionate share of the collection.

Distributing into buckets

To decide which bucket a value belongs in, the algorithm scales the value's position within the overall range by the number of buckets available.

Every element in the collection is examined once and placed into its corresponding bucket, in the order the buckets were created.

Sorting and combining

Once every element has been distributed, each bucket is sorted on its own, using insertion sort, since buckets are typically small.

The buckets are then combined back into a single collection, one after another, starting with the bucket covering the smallest range and ending with the bucket covering the largest range.

Because the buckets were created to cover non-overlapping, increasing ranges, and each bucket is itself sorted, the combined result is a fully sorted collection.

Example

Consider the sequence:

7, 3, 8, 2, 6

Suppose the values are divided into 3 buckets, covering the ranges 0-2, 3-5, and 6-8.

7, 8, and 6 fall into the third bucket. 3 falls into the second bucket. 2 falls into the first bucket.

Bucket 1 (0-2): 2
Bucket 2 (3-5): 3
Bucket 3 (6-8): 7, 8, 6

Bucket 1 and bucket 2 already contain a single element each, so they are already sorted.

Bucket 3 is sorted using insertion sort: 7 is followed by 8, which stays in place since it is already larger. Then 6 is considered: 8 is shifted right, 7 is shifted right, and 6 is placed at the front:

Bucket 3, sorted: 6, 7, 8

The buckets are combined in order:

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
