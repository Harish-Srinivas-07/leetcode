"""
Leetcode 437 - Path Sum III
https://leetcode.com/problems/path-sum-iii/
File: 437.path_sum_iii.py

Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000


"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------------


def path_sum_iii(root: Optional[TreeNode], targetSum: int) -> int:

    # helper dfs
    def dfs(node: Optional[TreeNode], target) -> int:
        if not node:
            return 0
        # count
        count = 1 if node.val == target else 0

        # count recursive - exclude current node val (qn)
        count += dfs(node.left, target - node.val)
        count += dfs(node.right, target - node.val)

        return count

    if not root:
        return 0

    total = dfs(root, targetSum)
    total += path_sum_iii(root.left, targetSum)
    total += path_sum_iii(root.right, targetSum)

    return total


# Alter solution -- too many time & space

    # def dfs(node: Optional[TreeNode], path_sum) -> int:
    #     if not node:
    #         return 0
    #     new_sum = [val + node.val for val in path_sum] + [node.val]

    #     count = new_sum.count(targetSum)

    #     count += dfs(node.left, new_sum)
    #     count += dfs(node.right, new_sum)

    #     return count

    # return dfs(root, [])


# ----------------------------------------------------------------
# Helper function to build a tree from level-order list
def build_tree(values):
    if not values:
        return None
    from collections import deque

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ----------------------------------------------------------------
if __name__ == "__main__":
    vals = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    target = 8
    root = build_tree(vals)
    print("Output:", path_sum_iii(root, target))  # Expected: 3
