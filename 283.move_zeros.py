"""
Leetcode 75 - 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
move_zeroes.py
ARRAY_STRING

Difficulty: Easy
Tags: Array, Two Pointers

Given an integer array `nums`, move all `0`'s to the end of the array **in-place**, while maintaining the relative order of the non-zero elements.
You are **not allowed** to make a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def solve(nums:list)-> list:
    pos = 0
    for i in range (len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos+=1
    print(pos)
    for i in range (pos,len(nums)):
        nums[i] = 0
    return nums

    # llama answer: working
    # write_index = 0

    # for read_index in range(len(nums)):
    #     if nums[read_index] != 0:
    #         nums[write_index], nums[read_index] = nums[read_index], nums[write_index]
    #         write_index += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(solve(nums))


"""
HINT

same as before done like vowels match -- get all non applicable elements from the array- then return final
"""
