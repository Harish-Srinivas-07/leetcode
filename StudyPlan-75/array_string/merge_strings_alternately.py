"""
Leetcode 75 - 1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Difficulty: Easy
Tags: String, Array, Two Pointers

You are given two strings word1 and word2.
Merge them by alternating characters from each, starting with word1.
Append remaining characters from the longer string.

Examples:
- Input:  word1 = "abc", word2 = "pqr"     → Output: "apbqcr"
- Input:  word1 = "ab",  word2 = "pqrs"    → Output: "apbqrs"
- Input:  word1 = "abcd", word2 = "pq"     → Output: "apbqcd"
"""

def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    i = 0
    while i < max(len(word1), len(word2)):
        if i < len(word1):
            res.append(word1[i])
        if i < len(word2):
            res.append(word2[i])
        i+=1
    return ''.join(res)


# ✅ Test cases
if __name__ == "__main__":
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"
    assert mergeAlternately("a", "xyz") == "axyz"
    assert mergeAlternately("hello", "") == "hello"
    assert mergeAlternately("", "world") == "world"
    print("All test cases passed ✅")
