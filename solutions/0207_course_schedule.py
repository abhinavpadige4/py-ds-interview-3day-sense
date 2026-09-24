"""
LeetCode 207 — Course Schedule
https://leetcode.com/problems/course-schedule/

Problem:
    There are a total of numCourses courses labeled 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [a, b]
    means you must take course b before course a.
    Return True if you can finish all courses (i.e., the graph is a DAG).

Pattern: Topological sort via Kahn's algorithm (BFS) or DFS cycle detection.
"""

from collections import defaultdict, deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Kahn's algorithm (BFS topological sort).

    - Build in-degree counts and adjacency list.
    - Repeatedly remove nodes with in-degree 0.
    - If we process all nodes, no cycle exists.

    Time:  O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    processed = 0
    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return processed == num_courses


def can_finish_dfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    DFS cycle detection with three states:
      0 = unvisited, 1 = in current path (back-edge = cycle), 2 = done.

    Time:  O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_courses

    def dfs(node) -> bool:
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return False  # back-edge -> cycle
            if color[neighbor] == WHITE and not dfs(neighbor):
                return False
        color[node] = BLACK
        return True

    for i in range(num_courses):
        if color[i] == WHITE and not dfs(i):
            return False
    return True


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(1, []) is True
    assert can_finish_dfs(2, [[1, 0]]) is True
    assert can_finish_dfs(2, [[1, 0], [0, 1]]) is False
    print("All tests passed.")
