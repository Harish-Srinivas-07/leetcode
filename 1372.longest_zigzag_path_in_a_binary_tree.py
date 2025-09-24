"""
Leetcode 1474 - Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
File: 1372.longest_zigzag_path_in_a_binary_tree.py

Difficulty: Medium
Tags: Dynamic Programming, Tree, Depth-First Search, Binary Tree

You are given the root of a binary tree.
A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100


"""

from typing import Optional
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------------


def longest_zigzag_path_in_a_binary_tree(root: Optional[TreeNode]) -> int:
    max_len = 0

    def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
        # use nonlocal keyword -- cause unreached
        nonlocal max_len
        
        if not node:
            return -1, -1 # -1 so that + 1 = 0

        left = dfs(node.left)
        right = dfs(node.right)

        left_len = left[1] + 1 # [1] zigzag left -> right
        right_len = right[0] + 1 # [0] zigzag right -> left

        max_len = max(max_len, left_len, right_len)

        return left_len, right_len

    dfs(root)
    return max_len


# ----------------------------------------------------------------
# Helper function to build a binary tree from level-order list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if node:
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


# ----------------------------------------------------------------
# Test cases
if __name__ == "__main__":
    # Test Case 1
    vals1 = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
    root1 = build_tree(vals1)
    print(
        "Output Test Case 1:", longest_zigzag_path_in_a_binary_tree(root1)
    )  # Expected: 3

    # Test Case 2
    vals2 = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    root2 = build_tree(vals2)
    print(
        "Output Test Case 2:", longest_zigzag_path_in_a_binary_tree(root2)
    )  # Expected: 4

    # Test Case 3
    vals3 = [1]
    root3 = build_tree(vals3)
    print(
        "Output Test Case 3:", longest_zigzag_path_in_a_binary_tree(root3)
    )  # Expected: 0
