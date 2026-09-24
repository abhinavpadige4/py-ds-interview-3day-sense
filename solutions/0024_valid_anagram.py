"""
LeetCode 24 — Valid Anagram
https://leetcode.com/problems/valid-anagram/

Problem:
    Given two strings s and t, return True if t is an anagram of s, else False.
    An anagram rearranges the letters of one string to form another.

Pattern: Character frequency counting (dict or collections.Counter).
"""

from collections import Counter
from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    """
    Frequency-count solution using Counter.

    Time:  O(n) — one pass over each string.
    Space: O(1) — at most 26 lowercase letters.
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def is_anagram_manual(s: str, t: str) -> bool:
    """
    Manual dict-based frequency count — shows the underlying mechanics.
    """
    if len(s) != len(t):
        return False

    freq: Dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True


def is_anagram_sort(s: str, t: str) -> bool:
    """
    Sort-and-compare. Simple but O(n log n) time.
    """
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram_manual("listen", "silent") is True
    assert is_anagram_sort("listen", "silent") is True
    print("All tests passed.")
