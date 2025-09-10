"""
Leetcode 2718 - Minimum Operations to Make All Array Elements Equal
https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
File: 2602.minimum_operations_to_make_all_array_elements_equal.py

Difficulty: Medium
Tags: Array, Binary Search, Sorting, Prefix Sum

You are given an array nums consisting of positive integers.
You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:

Increase or decrease an element of the array by 1.

Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].
Note that after each query the array is reset to its original state.

Example 1:

Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

Example 2:

Input: nums = [2,9,6,3], queries = [10]
Output: [20]
Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.


Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 105
1 <= nums[i], queries[i] <= 109


"""

from typing import List
from itertools import accumulate
from bisect import bisect_left


def minimum_operations_to_make_all_array_elements_equal(
    nums: List[int], queries: List[int]
) -> List[int]:
    n = len(nums)
    s = list(accumulate(nums, initial=0))
    result = []

    for q in queries:
        j = bisect_left(nums, q)

        # for all q> numbers left side -> increase part
        left = q * j - s[j]
        # for all q <= numbers right side -> decrease part
        right = s[n] - s[j] - q * (n - j)

        result.append(left + right)

    return result


if __name__ == "__main__":
    nums = [3, 1, 6, 8]
    queries = [1, 5]
    # nums = [2, 9, 6, 3]
    # queries = [10]
    print("Output:", minimum_operations_to_make_all_array_elements_equal(nums, queries))


"""
HINT : use binary search -> index (bisect_left)
get compute of left part & right part -> then append
---

Solved but failed at Time EXCEED

def minimum_operations_to_make_all_array_elements_equal(nums: List[int], queries: List[int]) -> List[int]:
    res = []
    for i in queries:
        res.append(findSum(nums, i))
    return res

def findSum(nums: List[int], k: int) -> int:
    sum = 0
    for n in enumerate(nums):
        sum += abs(n - k)
    return sum
    
---    
another solution:
# Sort the array to enable binary search and efficient calculation
nums.sort()

# Create prefix sum array with initial 0 for easier indexing
# prefix_sums[i] = sum of nums[0] to nums[i-1]
prefix_sums = list(accumulate(nums, initial=0))

result = []

for target in queries:
    # Find the first index where nums[index] > target
    # All elements from this index need to be decreased to target
    right_index = bisect_left(nums, target + 1)
    
    # Calculate operations needed to decrease all elements > target
    # Sum of (nums[i] - target) for all i where nums[i] > target
    decrease_operations = (prefix_sums[-1] - prefix_sums[right_index]) - (
        len(nums) - right_index
    ) * target

    # Find the first index where nums[index] >= target
    # All elements before this index need to be increased to target
    left_index = bisect_left(nums, target)

    # Calculate operations needed to increase all elements < target
    # Sum of (target - nums[i]) for all i where nums[i] < target
    increase_operations = target * left_index - prefix_sums[left_index]

    # Total operations is sum of increases and decreases
    total_operations = increase_operations + decrease_operations
    result.append(total_operations)

"""
