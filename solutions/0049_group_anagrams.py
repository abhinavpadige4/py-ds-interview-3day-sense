"""
LeetCode 49 — Group Anagrams
https://leetcode.com/problems/group-anagrams/

Problem:
    Given an array of strings, group anagrams together. Return the answer in
    any order.

Pattern: Hash-map keyed by a canonical form of each word.
"""

from collections import defaultdict
from typing import Dict, List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group by sorted characters. "eat" and "tea" both sort to "aet".

    Time:  O(n * k log k) where n = len(strs), k = max word length.
    Space: O(n * k) for the groups.
    """
    groups: Dict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_by_count(strs: List[str]) -> List[List[str]]:
    """
    Group by character-count tuple — O(n * k) instead of O(n * k log k).
    """
    groups: Dict[tuple, List[str]] = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(s)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result.sort(key=lambda g: sorted(g)[0])
    assert result == [["bat"], ["eat", "ate", "tea"], ["nat", "tan"]]

    result2 = group_anagrams_by_count(["eat", "tea", "tan", "ate", "nat", "bat"])
    result2.sort(key=lambda g: sorted(g)[0])
    assert result2 == [["bat"], ["eat", "ate", "tea"], ["nat", "tan"]]

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed.")
