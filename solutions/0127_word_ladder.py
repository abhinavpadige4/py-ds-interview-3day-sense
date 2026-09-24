"""
LeetCode 127 — Word Ladder
https://leetcode.com/problems/word-ladder/

Problem:
    Given two words beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence
    from beginWord to endWord such that only one letter is changed at a
    time and each intermediate word must exist in wordList. Return 0 if
    no such sequence exists.

Pattern: BFS on an implicit graph (each word is a node; edges connect
words that differ by exactly one letter).
"""

from collections import defaultdict, deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    BFS from beginWord. Each step changes one letter.

    Time:  O(N * L) where N = number of words, L = word length.
    Space: O(N * L)
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    word_set.discard(begin_word)

    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    while queue:
        word, steps = queue.popleft()
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == word[i]:
                    continue
                new_word = word[:i] + c + word[i + 1:]
                if new_word == end_word:
                    return steps + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0


def ladder_length_bidirectional(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Bidirectional BFS — expand from both ends, meet in the middle.
    Faster in practice for deep ladders.

    Time:  O(N * L)
    Space: O(N * L)
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    begin_set = {begin_word}
    end_set = {end_word}
    word_set.discard(begin_word)
    word_set.discard(end_word)
    steps = 1

    def expand(frontier):
        next_frontier = set()
        for word in frontier:
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in word_set:
                        word_set.discard(new_word)
                        next_frontier.add(new_word)
                    if new_word in end_set:
                        return True
        return next_frontier

    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set
        result = expand(begin_set)
        if isinstance(result, bool) and result:
            return steps + 1
        begin_set = result
        steps += 1
    return 0


if __name__ == "__main__":
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length("hit", "cog", words) == 4
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
    assert ladder_length_bidirectional("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
    print("All tests passed.")
