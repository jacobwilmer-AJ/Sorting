"""

Tree sort works by inserting every element of the collection into a binary search tree, and then reading the values back out in sorted order by traversing that tree.

A binary search tree is a structure in which every node holds one value, along with a link to a left subtree and a link to a right subtree. Every value in a node's left subtree is smaller than the node's own value, and every value in its right subtree is greater than or equal to it.

Inserting into the tree

To insert a value, the algorithm starts at the root of the tree. If there is no root yet, the value simply becomes the root.

Otherwise, the value is compared with the current node. If it is smaller, the algorithm moves to that node's left subtree; otherwise, it moves to the right subtree.

This comparison and move repeats at each node reached, always moving left for smaller values and right for values greater than or equal to the current node, until an empty spot is found.

The value is placed into that empty spot, becoming a new leaf of the tree.

Reading the values back out

Once every element has been inserted, the values are read back out in sorted order using an in-order traversal: for every node visited, first visit its entire left subtree, then the node itself, then its entire right subtree.

Because every value in a left subtree is smaller than the node, and every value in a right subtree is greater than or equal to it, visiting them in this left-node-right order naturally produces the values in ascending order.

Example

Consider the sequence:

7, 3, 8, 2, 6

7 is inserted first and becomes the root.

3 is compared with 7. Since it is smaller, it becomes 7's left child.

8 is compared with 7. Since it is not smaller, it becomes 7's right child.

2 is compared with 7, then with 3. Since it is smaller than both, it becomes 3's left child.

6 is compared with 7, then with 3. Since it is smaller than 7 but not smaller than 3, it becomes 3's right child.

The resulting tree is:

        7
       / \
      3   8
     / \
    2   6

Traversing this tree in order, left subtree first, then the node, then right subtree, visits the values in this order:

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
