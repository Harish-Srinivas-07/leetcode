"""
Leetcode 75 - 605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/
can_place_flowers.py
ARRAY_STRING

Difficulty: Easy
Tags: Array, Greedy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

from typing import List


def solve(flowerbed: List[int], n: int) -> bool:
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            left = flowerbed[i - 1] == 0 or i == 0
            right = flowerbed[i + 1] == 0 or i == len(flowerbed)
            if left and right:
                n -= 1
                if n == 0:
                    return True
                i += 1
        i += 1
    return n <= 0


if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print("Output:", solve(flowerbed, n))


"""
HINT

no need to track the array -- maintain the variable alone -- make check the left & right array element condition
"""
