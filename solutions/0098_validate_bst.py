"""
LeetCode 98 — Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Problem:
    Given the root of a binary tree, determine if it is a valid BST.
    A valid BST satisfies:
      - Left subtree contains only nodes with keys < node's key.
      - Right subtree contains only nodes with keys > node's key.
      - Both left and right subtrees are also valid BSTs.

Pattern: Recursive range check (min/max bounds).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Recursive range check. Each node must be within (low, high).

    Time:  O(n)
    Space: O(h) — recursion stack.
    """
    def validate(node, low=float("-inf"), high=float("inf")) -> bool:
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """
    Alternative: in-order traversal must produce a strictly increasing sequence.

    Time:  O(n)
    Space: O(h)
    """
    prev = float("-inf")

    def inorder(node):
        nonlocal prev
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= prev:
            return False
        prev = node.val
        return inorder(node.right)

    return inorder(root)


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
    # Valid BST
    assert is_valid_bst(build_tree([2, 1, 3])) is True
    # Invalid: right child 1 is not > 2
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False
    # Edge: single node
    assert is_valid_bst(build_tree([1])) is True
    assert is_valid_bst(None) is True
    # Duplicate values are not allowed in a strict BST
    assert is_valid_bst(build_tree([2, 2, 3])) is False
    assert is_valid_bst_inorder(build_tree([2, 1, 3])) is True
    assert is_valid_bst_inorder(build_tree([5, 1, 4, None, None, 3, 6])) is False
    print("All tests passed.")
