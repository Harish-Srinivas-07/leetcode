"""
Leetcode 904 - Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
File: 872.leaf_similar_trees.py

Difficulty: Easy
Tags: Tree, Depth-First Search, Binary Tree

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].


"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------------------------------------------


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # heper class to get all leaves
        def dfs(node: Optional[TreeNode]):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]

            leaves = []
            leaves.extend(dfs(node.left))
            leaves.extend(dfs(node.right))
            return leaves

        left = dfs(root1)
        right = dfs(root2)

        return left == right


# -------------------------------------------------------------------


# Helper function to build a tree from a list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
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


# Main function to update and test the code
if __name__ == "__main__":
    # Test Case 1
    root1_vals = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2_vals = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

    root1 = build_tree(root1_vals)
    root2 = build_tree(root2_vals)

    solution = Solution()
    print("Test Case 1 Output:", solution.leafSimilar(root1, root2))  # Output: True

    # Test Case 2
    root1_vals = [1, 2, 3]
    root2_vals = [1, 3, 2]

    root1 = build_tree(root1_vals)
    root2 = build_tree(root2_vals)

    print("Test Case 2 Output:", solution.leafSimilar(root1, root2))  # Output: False
