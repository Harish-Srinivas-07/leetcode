"""
Leetcode 1833 - Find the Highest Altitude  
https://leetcode.com/problems/find-the-highest-altitude/  
File: 1732.find_the_highest_altitude.py

Difficulty: Easy  
Tags: Array, Prefix Sum

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
 
Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

 
Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100


"""

from typing import List

def find_the_highest_altitude(gain:List) -> int:
    maxx = curr = 0 
    for i in range (len(gain)):
        curr += gain[i]
        maxx = max(curr, maxx)
    return maxx


if __name__ == "__main__":
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print("Output:", find_the_highest_altitude(gain))


"""
HINT
make 2 variable: one track sum, another make track max
"""