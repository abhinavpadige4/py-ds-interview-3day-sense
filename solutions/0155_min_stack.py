"""
LeetCode 155 — Min Stack
https://leetcode.com/problems/min-stack/

Problem:
    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

Pattern: Auxiliary min-stack (or store (value, current_min) pairs).
"""

from typing import Optional


class MinStack:
    """
    Stack with O(1) min retrieval.

    We maintain a parallel stack of running minimums. Each push updates
    the min-stack with min(new_value, current_min).

    Time:  O(1) for push, pop, top, get_min.
    Space: O(n)
    """

    def __init__(self):
        self.stack: list = []
        self.min_stack: list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


class MinStackPair:
    """
    Alternative: store (value, current_min) tuples on a single stack.

    Time:  O(1) for all operations.
    Space: O(n)
    """

    def __init__(self):
        self.stack: list = []  # list of (value, current_min)

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2

    ms2 = MinStackPair()
    ms2.push(5)
    ms2.push(3)
    ms2.push(7)
    assert ms2.get_min() == 3
    ms2.pop()
    assert ms2.top() == 3
    assert ms2.get_min() == 3
    print("All tests passed.")
