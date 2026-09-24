"""
LeetCode 26 — Remove Duplicates from Sorted Array (bonus: Contains Duplicate)
https://leetcode.com/problems/contains-duplicate/

Problem (Contains Duplicate):
    Given an integer array nums, return True if any value appears at least
    twice, else False.

Pattern: Hash set for O(1) membership.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Use a set to track seen values.

    Time:  O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_len(nums: List[int]) -> bool:
    """
    One-liner: if the set is smaller than the list, there's a duplicate.

    Time:  O(n)
    Space: O(n)
    """
    return len(set(nums)) < len(nums)


def contains_duplicate_sorted(nums: List[int]) -> bool:
    """
    If the array is sorted, compare adjacent elements.

    Time:  O(n) if already sorted, else O(n log n) to sort.
    Space: O(1) if in-place sort is allowed.
    """
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            return True
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([]) is False
    assert contains_duplicate_len([1, 2, 3, 1]) is True
    assert contains_duplicate_sorted([1, 2, 3, 1]) is True
    print("All tests passed.")
