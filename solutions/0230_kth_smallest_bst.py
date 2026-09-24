"""
LeetCode 230 — Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem:
    Given the root of a binary search tree and an integer k, return the kth
    smallest value (1-indexed) among all the values of the nodes.

Pattern: In-order traversal (produces sorted order for a BST).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    Iterative in-order traversal with a stack. Stop as soon as we've
    visited k nodes.

    Time:  O(h + k) where h is tree height.
    Space: O(h)
    """
    stack = []
    curr = root
    count = 0
    while stack or curr:
        # Go as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
    raise ValueError("k is out of range")


def kth_smallest_recursive(root: Optional[TreeNode], k: int) -> int:
    """
    Recursive in-order traversal with a counter.

    Time:  O(h + k)
    Space: O(h)
    """
    counter = [0]
    result = [None]

    def inorder(node):
        if not node or result[0] is not None:
            return
        inorder(node.left)
        counter[0] += 1
        if counter[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]


# ---------- Helpers for testing ----------
def build_tree(values):
    from collections import deque
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    # Tree: 3 -> (1, 5) -> (None, 2, 4, 6)
    tree = build_tree([3, 1, 5, None, None, 4, 6])
    assert kth_smallest(tree, 1) == 1
    assert kth_smallest(tree, 3) == 4
    assert kth_smallest_recursive(tree, 2) == 3

    tree2 = build_tree([1])
    assert kth_smallest(tree2, 1) == 1
    print("All tests passed.")
