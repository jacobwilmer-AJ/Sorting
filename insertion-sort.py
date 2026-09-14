"""

Insertion sort divides the collection conceptually into two sections:

A sorted section, which begins at the first element.
An unsorted section, containing everything after it.

Initially, the sorted section contains only the first element. A single element is considered sorted because there is nothing else with which it needs to be compared.

The algorithm then considers the elements in the unsorted section one at a time, from left to right.

For each element being considered, that element is called the key.

The key needs to be inserted into its correct position within the already-sorted section.

Inserting an element

Suppose the sorted section currently contains several elements in ascending order, and the next element to process is the key.

The algorithm starts by comparing the key with the element immediately to its left.

There are two possibilities.

If the element to the left is smaller than or equal to the key, then the key is already in its correct position. Nothing in the sorted section needs to move, and the sorted section can simply be considered one element larger.

If the element to the left is larger than the key, that larger element cannot remain immediately before the key. It must be moved one position to the right to make room for the key.

After moving that element, the algorithm looks at the element that was immediately before it and performs the same comparison.

This process continues toward the beginning of the sorted section:

Compare the key with the element immediately preceding its current position.
If that element is larger than the key, shift that element one position to the right.
Continue comparing the key with the next element farther to the left.
Keep shifting larger elements to the right for as long as necessary.
Stop when either the beginning of the sorted section is reached or an element is found that is smaller than or equal to the key.
Place the key into the position that has been created for it.

The important distinction is that elements are shifted rather than repeatedly swapped. The larger elements effectively move one position to the right as a group, creating a single open position into which the key is eventually placed.

Example

Consider the sequence:

7, 3, 8, 2, 6

Initially, only 7 is considered sorted:

[7] | 3, 8, 2, 6

The next element is 3. It is compared with 7. Since 7 is larger, 7 is shifted to the right and 3 is placed before it:

[3, 7] | 8, 2, 6

The next element is 8. It is compared with 7. Since 7 is not larger than 8, no shifting is necessary:

[3, 7, 8] | 2, 6

The next element is 2. It is smaller than 8, so 8 is shifted right. It is then compared with 7, which is also larger, so 7 is shifted right. It is then compared with 3, which is also larger, so 3 is shifted right. The beginning of the sorted section has now been reached, so 2 is placed at the beginning:

[2, 3, 7, 8] | 6

Finally, 6 is considered. It is smaller than 8, so 8 is shifted right. It is then compared with 7, which is also larger, so 7 is shifted right. It is then compared with 3, which is smaller, so the shifting stops and 6 is inserted between 3 and 7:

[2, 3, 6, 7, 8]

At this point every element has been processed, so the entire sequence is sorted.

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