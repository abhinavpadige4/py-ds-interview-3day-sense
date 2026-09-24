"""
LeetCode 215 — Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem:
    Given an integer array nums and an integer k, return the kth largest
    element in the array. Note: it's the kth largest element in the sorted
    order, not the kth distinct element.

Pattern: Min-heap of size k, or Quickselect.
"""

import heapq
import random
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Min-heap of size k. The top of the heap is the kth largest.

    Time:  O(n log k)
    Space: O(k)
    """
    heap: List[int] = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def find_kth_largest_sort(nums: List[int], k: int) -> int:
    """
    Sort and index. Simple but O(n log n).

    Time:  O(n log n)
    Space: O(1) or O(n) depending on sort.
    """
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k - 1]


def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Quickselect — average O(n), worst O(n^2).

    Time:  O(n) average
    Space: O(1) in-place
    """
    target_index = len(nums) - k  # kth largest = (n-k)th smallest (0-indexed)

    def partition(lo, hi):
        pivot = nums[random.randint(lo, hi)]
        nums[lo], nums[hi] = nums[hi], nums[lo]
        pivot_val = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot_val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = partition(lo, hi)
        if p == target_index:
            return nums[p]
        elif p < target_index:
            lo = p + 1
        else:
            hi = p - 1
    raise ValueError("k is out of range")


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest_sort([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest_quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("All tests passed.")
