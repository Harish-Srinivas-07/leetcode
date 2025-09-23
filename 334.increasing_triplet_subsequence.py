"""
Leetcode 334 - Increasing Triplet Subsequence  
https://leetcode.com/problems/increasing-triplet-subsequence/  
File: 334.increasing_triplet_subsequence.py

Difficulty: Medium  
Tags: Array, Greedy

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

 
Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""


from typing import List


def increasing_triplet_subsequence(nums: List[int]) -> bool:
    first = second = float('inf')
    
    for n in nums:
        if first >= n:
            first = n
        elif second >= n :
            second = n
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]  # true
    nums = [5, 4, 3, 2, 1] # false
    nums = [2, 1, 5, 0, 4, 6]  # true
    print("Output:", increasing_triplet_subsequence(nums))
