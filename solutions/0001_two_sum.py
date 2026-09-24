"""
LeetCode 1 — Two Sum
https://leetcode.com/problems/two-sum/

Problem:
    Given an array of integers `nums` and an integer `target`, return indices of
    the two numbers such that they add up to `target`. Exactly one solution
    exists; you may not use the same element twice.

Pattern: Hash-map single-pass lookup.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Single-pass hash-map solution.

    For each number, check if (target - num) has already been seen. If yes,
    return the stored index and the current index. Otherwise, store the
    current number -> index mapping.

    Time:  O(n) — one pass, O(1) dict lookups.
    Space: O(n) — worst case we store every element.
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # unreachable given problem constraints


# ---------- Brute-force alternative (for reference) ----------
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    O(n^2) nested-loop solution. Correct but too slow for large inputs.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    # Examples from LeetCode
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 5, 1, 1, 6, 9], 10) == [4, 5]
    print("All tests passed.")
