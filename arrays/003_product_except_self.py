# Problem: Product of Array Except Self (LeetCode #238)
# Difficulty: Medium
# Pattern: Prefix and Suffix Products
# Date: 2026-09-12

# Question:
# Given an integer array nums, return an array where each element
# is the product of all other elements except itself.
# Constraint: Do NOT use division. Must be O(n).

# Approach:
# Two passes through the array.
# Pass 1: build prefix products (everything to the LEFT of index i)
# Pass 2: multiply by suffix products (everything to the RIGHT of index i)
# Time: O(n) | Space: O(1) excluding output array

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right pass: multiply by product of all elements right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Tests
print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]