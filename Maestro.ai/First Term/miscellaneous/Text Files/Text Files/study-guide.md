# Data Structures Quiz Study Guide (Goal: 18/20+)

Current score: 14/20
Target: Fix 6 missed concepts with high-yield review.

## What To Fix First

1. Hash map and set average-case performance rules.
2. Dynamic array insertion cost when not appending.
3. Linked list access cost by index.

## Core Concept Corrections (From Missed Questions)

1. Singly linked list index access is O(n), not O(1).
Reason: You must walk node-by-node from the head to reach index k.

2. Hash map key lookup is typically O(1) on average.
Why: Good hash function + controlled load factor keeps buckets short.

3. Set guarantee: unique elements only (no duplicates).

4. Dynamic array insertion at index i is O(n) in the worst case.
Reason: Elements after i must shift right.

5. Hash maps resize (rehash) to keep load factor low.
Result: Preserves near O(1) average insert/find/delete.

6. Set membership tests are typically O(1) on average.

## Common Traps

1. Confusing average-case with worst-case.
Tip: If a question says "typically" or "on average," think hash table O(1).

2. Assuming arrays are O(1) for all insertions.
Tip: Only append can be O(1) amortized; middle insert is O(n).

3. Mixing up set properties with list/array properties.
Tip: Set = uniqueness, not index order.

4. Forgetting traversal cost in linked lists.
Tip: Linked list random access is not constant time.

## Memory Cues

1. Linked list index = "line walk" -> O(n)
2. Hash map average lookup = "one bucket, fast check" -> O(1)
3. Set = "single copy only"
4. Array middle insert = "shift crowd" -> O(n)
5. Rehash = "spread keys out again"

## 10-Minute Review Drill

Spend about 1 minute per item.

1. Why is singly linked list access by index O(n)?
2. In a hash map, what conditions make lookup O(1) average?
3. What does a set guarantee about duplicates?
4. Why is dynamic array insertion at index i (not end) O(n)?
5. Why do hash maps rehash as they grow?
6. What is typical set membership complexity and why?
7. Which is faster for random index access: array or linked list? Why?
8. Append vs middle insert in dynamic array: compare complexities.
9. What does load factor influence in hash tables?
10. Give one example of average-case vs worst-case in hashing.

## Drill Answer Key (Quick Check)

1. Must traverse from head through nodes -> O(n).
2. Good hash distribution and low load factor.
3. No duplicates; elements are unique.
4. Must shift later elements right -> O(n).
5. Keep load factor low to preserve O(1) average operations.
6. O(1) average due to hash-based lookup.
7. Array, because indexing is O(1); linked list index access is O(n).
8. Append: O(1) amortized. Middle insert: O(n).
9. Collision frequency and operation speed.
10. Average lookup O(1), worst-case O(n) with heavy collisions.

## Quiz-Day Execution Strategy

1. First pass: answer direct definition questions immediately.
2. Second pass: handle complexity comparison questions carefully.
3. Final pass: scan for trigger words: average, worst-case, amortized, unique, load factor.
4. If two answers seem close, pick the one matching the data structure mechanics (traversal, shifting, hashing).

## 24-Hour Prep Plan

1. Morning (10 minutes): read Core Concept Corrections once.
2. Afternoon (10 minutes): do the 10-minute drill from memory.
3. Evening (10 minutes): redo only missed drill questions.
4. Pre-quiz (5 minutes): read Memory Cues and trigger words.
