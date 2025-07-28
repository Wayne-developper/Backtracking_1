# Leetcode 78 - Subsets
This reportory contains two python solution to the problem  [Leetcode 78 - Subsets](https://leetcode.com/problems/subsets/).

## 🧠 Problem
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

## 🗂️ Files
- 'First_test.py' - backtracking solution
- 'Optimized_test.py' - iterative optimized solution

## 🚀 Approaches
## 1. Backtracking (Recursive)
- Explore all combinations by including or skipping elements
- Recursive tree traversal with `path` and `start` index
- Good for understanding recursion

### 2. Iterative (Optimized)
- Starts with an empty subset: `[[]]`
- For each number in `nums`, adds it to every existing subset
- No recursion, faster in execution

## 💡 Example

```python
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
