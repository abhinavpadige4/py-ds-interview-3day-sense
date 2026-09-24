"""
LeetCode 104 — Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
    Given the root of a binary tree, return its maximum depth.
    The maximum depth is the number of nodes along the longest path from
    the root node down to the farthest leaf node.

Pattern: DFS recursion (or BFS level count).
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Recursive DFS.

    Time:  O(n)
    Space: O(h) — recursion stack, h = tree height.
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """
    Iterative DFS with an explicit stack.

    Time:  O(n)
    Space: O(h)
    """
    if not root:
        return 0
    stack = [(root, 1)]
    depth = 0
    while stack:
        node, d = stack.pop()
        depth = max(depth, d)
        if node.left:
            stack.append((node.left, d + 1))
        if node.right:
            stack.append((node.right, d + 1))
    return depth


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    BFS level count.

    Time:  O(n)
    Space: O(n)
    """
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


# ---------- Helpers for testing ----------
def build_tree(values):
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
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(build_tree([1, None, 2])) == 2
    assert max_depth(None) == 0
    assert max_depth_iterative(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth_bfs(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    print("All tests passed.")
