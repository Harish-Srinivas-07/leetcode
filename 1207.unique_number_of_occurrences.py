"""
Leetcode 1319 - Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
File: 1207.unique_number_of_occurrences.py

Difficulty: Easy
Tags: Array, Hash Table

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


"""

from typing import List


def unique_number_of_occurrences(arr: List[int]) -> bool:
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    count = freq.values()
    return len(count) == len(set(count))


if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    # arr = [1, 2]
    # arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print("Output:", unique_number_of_occurrences(arr))


""""
HINT
recommended using freq : its clear must use freq --- try without a counter

INEFFIECENT CODE BUT PASSED
def unique_number_of_occurrences(arr: List[int]) -> bool:
    visited = set()
    values = []
    for i in arr:
        if i not in visited:
            values.append(arr.count(i))
            visited.add(i)
    return len(values) == len(set(values))
"""
