"""
LeetCode 232 — Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Problem:
    Implement a first-in-first-out (FIFO) queue using only two stacks.
    The queue should support all usual operations: push, pop, peek, and empty.

Pattern: Two-stack amortized O(1) queue.
"""

from typing import Optional


class MyQueue:
    """
    Two-stack queue.

    - `in_stack` receives new pushes.
    - `out_stack` is used for pops/peeks.
    - When `out_stack` is empty, transfer all elements from `in_stack`
      to `out_stack` (reversing order).

    Amortized time: O(1) per operation.
    Space: O(n)
    """

    def __init__(self):
        self.in_stack: list = []
        self.out_stack: list = []

    def _transfer(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True

    # Interleaved push/pop
    q2 = MyQueue()
    q2.push(1)
    q2.push(2)
    q2.pop()  # 1
    q2.push(3)
    q2.push(4)
    assert q2.pop() == 2
    assert q2.pop() == 3
    assert q2.pop() == 4
    assert q2.empty() is True
    print("All tests passed.")
