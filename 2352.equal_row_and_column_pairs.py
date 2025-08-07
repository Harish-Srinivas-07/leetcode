"""
Leetcode 2428 - Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/
File: 2352.equal_row_and_column_pairs.py

Difficulty: Medium
Tags: Array, Hash Table, Matrix, Simulation

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105


"""

from typing import List


def equal_row_and_column_pairs(grid: List[List[int]]) -> int:
    n = len(grid)

    freq = {}

    # get freq for the row (tuple)
    for row in grid:
        tp = tuple(row)
        freq[tp] = freq.get(tp, 0) + 1

    ans = 0

    # now trans row count
    for row in range(n):
        col = tuple(grid[r][row] for r in range(n))
        ans += freq.get(col, 0)

    return ans


if __name__ == "__main__":
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print("Output:", equal_row_and_column_pairs(grid))
