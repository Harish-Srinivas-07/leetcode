"""
Leetcode 11 - Container With Most Water  
https://leetcode.com/problems/container-with-most-water/  
File: 11.container_with_most_water.py

Difficulty: Medium  
Tags: Array, Two Pointers, Greedy

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
 
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""
from typing import List

def container_with_most_water(height: List[int]) -> int:
    max_area = 1
    i = 0
    j = len(height)-1
    while i < j:
        left = height[i]
        right = height[j]
        area = min(left, right) * (j-i)
        max_area = max(area, max_area)
        
        if left < right:
            i+=1
        else:
            j-=1
    return max_area
    


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Output:", container_with_most_water(height))
