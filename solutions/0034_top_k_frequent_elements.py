"""
LeetCode 34 — Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Problem:
    Given an integer array nums and an integer k, return the k most frequent
    elements. You may return the answer in any order.

Pattern: Hash-map counting + heap (or bucket sort).
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Counter + heap.nlargest. Clean and idiomatic.

    Time:  O(n + k log n) — count in O(n), nlargest in O(k log n).
    Space: O(n) for the counter.
    """
    counts = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]


def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    """
    Bucket sort by frequency — O(n) time.

    Time:  O(n)
    Space: O(n)
    """
    counts = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result: List[int] = []
    for freq in range(len(buckets) - 1, -1, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Manual min-heap of size k — keeps only the top-k seen so far.

    Time:  O(n log k)
    Space: O(k)
    """
    counts = Counter(nums)
    heap: List[tuple] = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent_bucket([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("All tests passed.")
