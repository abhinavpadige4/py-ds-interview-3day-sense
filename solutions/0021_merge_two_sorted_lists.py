"""
LeetCode 21 — Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
    Given the heads of two sorted linked lists, merge them into a single
    sorted list by splicing together the nodes. Return the head of the merged list.

Pattern: Dummy-node merge (like merge step of merge sort).
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iterative merge using a dummy head.

    Time:  O(n + m)
    Space: O(1) — only pointer manipulation.
    """
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # Attach the remaining tail of whichever list is non-empty
    tail.next = l1 if l1 else l2
    return dummy.next


def merge_two_lists_recursive(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Recursive merge.

    Time:  O(n + m)
    Space: O(n + m) — recursion stack.
    """
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursive(l1, l2.next)
        return l2


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
    assert to_list(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two_lists(build_list([]), build_list([]))) == []
    assert to_list(merge_two_lists(build_list([]), build_list([0]))) == [0]
    assert to_list(merge_two_lists_recursive(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    print("All tests passed.")
