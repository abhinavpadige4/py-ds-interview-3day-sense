"""
LeetCode 102 — Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem:
    Given the root of a binary tree, return the level order traversal of its
    nodes' values (left-to-right, level-by-level).

Pattern: BFS with a queue (collections.deque).
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    BFS level-order traversal.

    Time:  O(n) — visit every node once.
    Space: O(n) — queue holds at most one level.
    """
    if not root:
        return []
    result: List[List[int]] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def level_order_dfs(root: Optional[TreeNode]) -> List[List[int]]:
    """
    DFS alternative — track depth and append to result[level].

    Time:  O(n)
    Space: O(n) — recursion stack + result.
    """
    result: List[List[int]] = []

    def dfs(node, depth):
        if not node:
            return
        if depth == len(result):
            result.append([])
        result[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result


# ---------- Helpers for testing ----------
def build_tree(values):
    """Build a tree from a level-order list with None for missing nodes."""
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
    tree = build_tree([3, 9, 20, None, None, 15, 7])
    assert level_order(tree) == [[3], [9, 20], [15, 7]]
    assert level_order_dfs(tree) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(None) == []
    print("All tests passed.")
