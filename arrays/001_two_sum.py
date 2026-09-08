# Problem: Two Sum (LeetCode #1)
# Difficulty: Easy
# Pattern: HashMap
# Date: 2026-09-08

# Question:
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.

# Approach:
# Use a hashmap to store each number and its index.
# For each number, check if the complement (target - num)
# already exists in the hashmap.
# Time: O(n) | Space: O(n)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(two_sum([3, 2, 4], 6))       # Expected: [1, 2]