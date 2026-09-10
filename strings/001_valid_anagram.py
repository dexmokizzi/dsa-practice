# Problem: Valid Anagram (LeetCode #242)
# Difficulty: Easy
# Pattern: HashMap / Counter
# Date: 2026-09-10

# Question:
# Given two strings s and t, return True if t is an anagram of s.
# An anagram uses the same letters in the same quantities.

# Approach:
# Count character frequencies in both strings using Counter.
# If the frequency maps are equal, they are anagrams.
# Time: O(n) | Space: O(n)

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Tests
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("listen", "silent"))    # True