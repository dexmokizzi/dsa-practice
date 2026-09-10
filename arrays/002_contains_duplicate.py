# Problem: Contains Duplicate (LeetCode #217)
# Difficulty: Easy
# Pattern: HashMap / HashSet
# Date: 2026-09-09

# Question:
# Given an integer array nums, return True if any value
# appears at least twice, and False if every element is distinct.

# Approach:
# Use a set to track seen numbers.
# If a number is already in the set, we have a duplicate.
# Time: O(n) | Space: O(n)

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# One-liner alternative (Pythonic)
# return len(nums) != len(set(nums))

# Tests
print(contains_duplicate([1, 2, 3, 1]))   # True
print(contains_duplicate([1, 2, 3, 4]))   # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True