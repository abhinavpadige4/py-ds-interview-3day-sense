"""
LeetCode 167 — Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem:
    Given a 1-indexed array of integers `numbers` sorted in non-decreasing
    order, find two numbers such that they add up to a target. Return the
    two indices (1-indexed) as an array of length 2.

Pattern: Two-pointer on a sorted array.
"""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Two-pointer approach: start at both ends, move inward.

    - If sum < target, move left pointer right (need bigger sum).
    - If sum > target, move right pointer left (need smaller sum).
    - If sum == target, return 1-indexed positions.

    Time:  O(n)
    Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


def two_sum_sorted_binary_search(numbers: List[int], target: int) -> List[int]:
    """
    Alternative: for each element, binary-search for its complement.

    Time:  O(n log n)
    Space: O(1)
    """
    n = len(numbers)
    for i in range(n):
        complement = target - numbers[i]
        # Binary search in (i+1, n)
        lo, hi = i + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                lo = mid + 1
            else:
                hi = mid - 1
    return []


if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([-1, 0, 1, 0, 8, 7], 9) == [2, 5]
    assert two_sum_sorted([3, 24, 35, 46, 50], 81) == [2, 4]
    assert two_sum_sorted_binary_search([2, 7, 11, 15], 9) == [1, 2]
    print("All tests passed.")
