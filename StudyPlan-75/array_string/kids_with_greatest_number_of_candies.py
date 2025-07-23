"""
Leetcode 75 - 1431. Kids With the Greatest Number of Candies  
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
kids_with_greatest_number_of_candies.py

Difficulty: Easy  
Tags: Array

There are n kids with candies. You are given an integer array `candies`, where `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`.  
Return a boolean array where each element is `True` if, after giving the ith kid all the `extraCandies`, they will have the greatest number of candies among all the kids.

Examples:
- Input: candies = [2,3,5,1,3], extraCandies = 3     → Output: [true,true,true,false,true]
- Input: candies = [4,2,1,1,2], extraCandies = 1     → Output: [true,false,false,false,false]
- Input: candies = [12,1,12], extraCandies = 10      → Output: [true,false,true]
"""