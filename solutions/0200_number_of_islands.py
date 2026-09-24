"""
LeetCode 200 — Number of Islands
https://leetcode.com/problems/number-of-islands/

Problem:
    Given an m x n 2D grid map of '1's (land) and '0's (water), return the
    number of islands. An island is surrounded by water and formed by
    connecting adjacent lands horizontally or vertically.

Pattern: DFS/BFS flood-fill on a grid (graph traversal).
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    DFS flood-fill. Mark visited cells by mutating the grid to '0'.

    Time:  O(m * n)
    Space: O(m * n) worst case for recursion stack.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"  # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count


def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    BFS flood-fill using a deque.

    Time:  O(m * n)
    Space: O(m * n)
    """
    from collections import deque
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                grid[r][c] = "0"
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            queue.append((nx, ny))
    return count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands([row[:] for row in grid1]) == 3
    assert num_islands_bfs([row[:] for row in grid1]) == 3

    grid2 = [["0", "0"], ["0", "0"]]
    assert num_islands(grid2) == 0

    grid3 = [["1"]]
    assert num_islands(grid3) == 1
    print("All tests passed.")
