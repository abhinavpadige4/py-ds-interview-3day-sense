"""
LeetCode 20 — Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '['
    and ']', determine if the input string is valid.

Pattern: Stack-based matching.
"""


def is_valid(s: str) -> bool:
    """
    Use a stack to match closing brackets with the most recent opening bracket.

    Time:  O(n)
    Space: O(n) — worst case all opening brackets.
    """
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in pairs:  # closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:  # opening bracket
            stack.append(ch)
    return len(stack) == 0


def is_valid_counter(s: str) -> bool:
    """
    Alternative: count each bracket type. Only works if brackets are
    properly nested in a specific way — NOT a general solution.
    Included for contrast; prefer the stack approach.
    """
    counts = {"(": 0, "[": 0, "{": 0}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        elif ch == ")":
            counts["("] -= 1
        elif ch == "]":
            counts["["] -= 1
        elif ch == "}":
            counts["{"] -= 1
        if any(v < 0 for v in counts.values()):
            return False
    return all(v == 0 for v in counts.values())


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(") is False
    assert is_valid(")") is False
    print("All tests passed.")
