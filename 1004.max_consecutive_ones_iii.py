"""
Leetcode 1046 - Max Consecutive Ones III  
https://leetcode.com/problems/max-consecutive-ones-iii/  
File: 1004.max_consecutive_ones_iii.py

Difficulty: Medium  
Tags: Array, Binary Search, Sliding Window, Prefix Sum

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length


"""
from typing import List

def max_consecutive_ones_iii(nums: List[int], k: int)-> int:
    maxx = left = zero = 0
    for right in range (len(nums)):
        if nums[right] == 0:
            zero +=1 
        while zero > k:
            if nums[left] == 0:
                zero -=1
            left +=1
        maxx = max(maxx, right-left+1)
    return maxx


if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2 
    print("Output:", max_consecutive_ones_iii(nums,k))


"""
HINT
obviously sliding window -- but the right side is flex -- so make a loop over right
"""