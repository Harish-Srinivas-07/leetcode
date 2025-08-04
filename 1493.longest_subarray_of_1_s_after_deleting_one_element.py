"""
Leetcode 1586 - Longest Subarray of 1's After Deleting One Element  
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/  
File: 1493.longest_subarray_of_1_s_after_deleting_one_element.py

Difficulty: Medium  
Tags: Array, Dynamic Programming, Sliding Window

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
 
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


"""
from typing import List

def longest_subarray_of_1_s_after_deleting_one_element(nums : List[int])-> int:
    maxx = left = zero = 0
    for right in range (len(nums)):
        if nums[right] == 0:
            zero+=1
        while zero > 1:
            if nums[left] == 0:
                zero-=1
            left +=1
        maxx = max(maxx, right-left)
    return maxx

if __name__ == "__main__":
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print("Output:", longest_subarray_of_1_s_after_deleting_one_element(nums))

"""
HINT
sliding window -- obviously right side is flex -- so same as the LT:1004 Max Consecutive-iii
"""