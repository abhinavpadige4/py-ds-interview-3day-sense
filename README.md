# Python Data Structures — 3-Day Interview Prep

A focused, pattern-driven 3-day plan to get interview-ready on Python data structures.
21 LeetCode problems, one per file, each with a clean solution, complexity analysis,
and a short "why this matters in an interview" note.

## The 3-Day Plan

### Day 1 — Built-ins: Lists, Dicts, Sets, Tuples
Master the operations you'll use 80% of the time. Focus on **time complexity of each
operation** and the classic patterns (two-pointer, sliding window, hash-map counting).

| # | Problem | File |
|---|---------|------|
| 1 | Two Sum | [solutions/0001_two_sum.py](solutions/0001_two_sum.py) |
| 2 | Valid Anagram | [solutions/0024_valid_anagram.py](solutions/0024_valid_anagram.py) |
| 3 | Group Anagrams | [solutions/0049_group_anagrams.py](solutions/0049_group_anagrams.py) |
| 4 | Top K Frequent Elements | [solutions/0034_top_k_frequent_elements.py](solutions/0034_top_k_frequent_elements.py) |
| 5 | Contains Duplicate | [solutions/0217_contains_duplicate.py](solutions/0217_contains_duplicate.py) |
| 6 | Two Sum II (Sorted Array) | [solutions/0167_two_sum_ii.py](solutions/0167_two_sum_ii.py) |

### Day 2 — Linked Lists, Stacks, Queues
Pointer manipulation and LIFO/FIFO mechanics. Implement the structures from scratch
before reaching for `collections.deque`.

| # | Problem | File |
|---|---------|------|
| 7 | Reverse Linked List | [solutions/0206_reverse_linked_list.py](solutions/0206_reverse_linked_list.py) |
| 8 | Merge Two Sorted Lists | [solutions/0021_merge_two_sorted_lists.py](solutions/0021_merge_two_sorted_lists.py) |
| 9 | Linked List Cycle | [solutions/0141_linked_list_cycle.py](solutions/0141_linked_list_cycle.py) |
| 10 | Valid Parentheses | [solutions/0020_valid_parentheses.py](solutions/0020_valid_parentheses.py) |
| 11 | Min Stack | [solutions/0155_min_stack.py](solutions/0155_min_stack.py) |
| 12 | Implement Queue using Stacks | [solutions/0232_implement_queue_using_stacks.py](solutions/0232_implement_queue_using_stacks.py) |

### Day 3 — Trees, Heaps, Graphs
Recursion, BST invariants, heap-based top-K, and BFS/DFS on graphs.

| # | Problem | File |
|---|---------|------|
| 13 | Binary Tree Level Order Traversal | [solutions/0102_level_order_traversal.py](solutions/0102_level_order_traversal.py) |
| 14 | Maximum Depth of Binary Tree | [solutions/0104_max_depth.py](solutions/0104_max_depth.py) |
| 15 | Validate Binary Search Tree | [solutions/0098_validate_bst.py](solutions/0098_validate_bst.py) |
| 16 | Kth Smallest Element in a BST | [solutions/0230_kth_smallest_bst.py](solutions/0230_kth_smallest_bst.py) |
| 17 | Kth Largest Element in an Array | [solutions/0215_kth_largest.py](solutions/0215_kth_largest.py) |
| 18 | Number of Islands | [solutions/0200_number_of_islands.py](solutions/0200_number_of_islands.py) |
| 19 | Course Schedule (Topological Sort) | [solutions/0207_course_schedule.py](solutions/0207_course_schedule.py) |
| 20 | Clone Graph | [solutions/0133_clone_graph.py](solutions/0133_clone_graph.py) |
| 21 | Word Ladder | [solutions/0127_word_ladder.py](solutions/0127_word_ladder.py) |

## How to use this repo

1. **Read the plan** for the day, then open each solution file.
2. **Don't read the code first** — try the problem for 15 minutes, then compare.
3. **Re-implement from memory** the next day before moving on.
4. Each file has:
   - Problem statement (short)
   - Solution with comments
   - Time & space complexity
   - Interview talking points

## Complexity cheat sheet

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| List (array) | O(1) | O(n) | O(1) amortized | O(n) |
| Dict (hash map) | — | O(1) avg | O(1) avg | O(1) avg |
| Set (hash set) | — | O(1) avg | O(1) avg | O(1) avg |
| Tuple | O(1) | O(n) | immutable | immutable |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | — | O(n) | O(1) | O(1) |
| Queue (deque) | — | O(n) | O(1) | O(1) |
| BST | — | O(log n) avg | O(log n) avg | O(log n) avg |
| Heap | — | O(n) | O(log n) | O(log n) |
| Graph (adj list) | — | O(V+E) | O(1) | O(1) |

## Concepts covered

- Arrays & lists, two-pointer, sliding window
- Hash maps, hash sets, frequency counting
- Linked lists, fast/slow pointers, cycle detection
- Stacks (LIFO), queues (FIFO), monotonic stacks
- Binary trees, BFS level-order, DFS recursion, BST invariants
- Heaps (min/max), top-K patterns
- Graphs: BFS, DFS, topological sort, cycle detection, connected components
