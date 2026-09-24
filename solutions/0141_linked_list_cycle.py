"""
LeetCode 141 — Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Problem:
    Given the head of a linked list, determine if the linked list has a cycle.
    A cycle exists if some node can be reached again by following next pointers.

Pattern: Floyd's tortoise-and-hare (fast/slow pointers).
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Floyd's cycle detection.

    - Slow moves 1 step, fast moves 2 steps.
    - If there's a cycle, they must meet inside it.
    - If fast reaches the end, no cycle.

    Time:  O(n)
    Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def has_cycle_set(head: Optional[ListNode]) -> bool:
    """
    Alternative: track visited nodes in a set.

    Time:  O(n)
    Space: O(n)
    """
    seen = set()
    curr = head
    while curr:
        if id(curr) in seen:
            return True
        seen.add(id(curr))
        curr = curr.next
    return False


# ---------- Helpers for testing ----------
def build_list_with_cycle(values, cycle_pos=None):
    """Build a list; if cycle_pos is not None, tail points to node at that index."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos is not None:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


if __name__ == "__main__":
    # 3 -> 2 -> 0 -> -4 -> 2 (cycle back to index 1)
    assert has_cycle(build_list_with_cycle([3, 2, 0, -4], cycle_pos=1)) is True
    # 1 -> 2 -> 1 (cycle back to index 0)
    assert has_cycle(build_list_with_cycle([1, 2], cycle_pos=0)) is True
    # No cycle
    assert has_cycle(build_list_with_cycle([1, 2, 3, 4])) is False
    assert has_cycle(build_list_with_cycle([1])) is False
    assert has_cycle(None) is False
    assert has_cycle_set(build_list_with_cycle([3, 2, 0, -4], cycle_pos=1)) is True
    print("All tests passed.")
