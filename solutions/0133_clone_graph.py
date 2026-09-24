"""
LeetCode 133 — Clone Graph
https://leetcode.com/problems/clone-graph/

Problem:
    Given a reference to a node in a connected undirected graph, return a
    deep copy (clone) of the graph. Each node has a value and a list of
    neighbors.

Pattern: DFS/BFS with a visited map (original -> clone).
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    DFS with a visited dict mapping original nodes to their clones.

    Time:  O(V + E)
    Space: O(V)
    """
    if not node:
        return None

    visited = {}

    def dfs(original: Node) -> Node:
        if original in visited:
            return visited[original]
        clone = Node(original.val)
        visited[original] = clone
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    BFS with a visited dict.

    Time:  O(V + E)
    Space: O(V)
    """
    from collections import deque
    if not node:
        return None

    visited = {node: Node(node.val)}
    queue = deque([node])
    while queue:
        original = queue.popleft()
        for neighbor in original.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            visited[original].neighbors.append(visited[neighbor])
    return visited[node]


# ---------- Helpers for testing ----------
def build_cycle_graph(n):
    """Build a cycle graph with n nodes (1..n), each connected to its neighbors."""
    if n == 0:
        return None
    nodes = [Node(i) for i in range(1, n + 1)]
    for i in range(n):
        nodes[i].neighbors = [nodes[(i - 1) % n], nodes[(i + 1) % n]]
    return nodes[0]


def graph_signature(node):
    """Return a canonical signature of the graph rooted at node."""
    if not node:
        return None
    visited = set()
    stack = [node]
    edges = set()
    while stack:
        n = stack.pop()
        if id(n) in visited:
            continue
        visited.add(id(n))
        for nb in n.neighbors:
            edges.add((n.val, nb.val))
            stack.append(nb)
    return (len(visited), frozenset(edges))


if __name__ == "__main__":
    # 4-node cycle: 1-2-3-4-1
    original = build_cycle_graph(4)
    clone = clone_graph(original)
    assert graph_signature(original) == graph_signature(clone)
    assert clone is not original
    assert clone.neighbors[0] is not original.neighbors[0]

    clone_bfs = clone_graph_bfs(original)
    assert graph_signature(original) == graph_signature(clone_bfs)

    assert clone_graph(None) is None
    print("All tests passed.")
