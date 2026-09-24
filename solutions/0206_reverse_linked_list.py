"""
LeetCode 206 — Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Problem:
    Given the head of a singly linked list, reverse the list and return the
    reversed list.

Pattern: Iterative pointer reversal (or recursion).
"""

from typing import Optional


class ListNode:
    """Standard singly-linked-list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iterative reversal using three pointers: prev, curr, next_node.

    For each node, redirect its .next to the previous node, then advance.

    Time:  O(n)
    Space: O(1)
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # save next
        curr.next = prev       # reverse link
        prev = curr            # advance prev
        curr = next_node       # advance curr
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Recursive reversal. Base case: empty or single-node list.

    Time:  O(n)
    Space: O(n) — recursion stack.
    """
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# ---------- Helpers for testing ----------
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build_list([1, 2]))) == [2, 1]
    assert to_list(reverse_list(build_list([1]))) == [1]
    assert to_list(reverse_list(build_list([]))) == []
    assert to_list(reverse_list_recursive(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    print("All tests passed.")
