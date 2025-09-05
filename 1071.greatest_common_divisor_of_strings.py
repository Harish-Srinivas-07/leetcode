"""
Leetcode 75 - 1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
greatest_common_divisor_of_strings.py
ARRAY_STRING

Difficulty: Easy
Tags: String, Math, GCD

For two strings s and t, we say "t divides s" if and only if:
  s == t + t + t + ... + t  (one or more times)

Return the largest string x such that x divides both str1 and str2.

Examples:
- Input:  str1 = "ABCABC", str2 = "ABC"     → Output: "ABC"
- Input:  str1 = "ABABAB", str2 = "ABAB"    → Output: "AB"
- Input:  str1 = "LEET", str2 = "CODE"      → Output: ""
"""

import math


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[: math.gcd(len(str1), len(str2))]


if __name__ == "__main__":
    # str1 = input("Enter str1: ").strip()
    # str2 = input("Enter str2: ").strip()
    # print("Output:", gcdOfStrings(str1, str2))

    # Optional test cases
    assert gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert gcdOfStrings("LEET", "CODE") == ""
    print("All test cases passed ✅")
