"""
Leetcode 236 - Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
File: 236.lowest_common_ancestor_of_a_binary_tree.py

Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.


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


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:

    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right


# ----------------------------------------------------------------
# Helper to build a tree from level-order list
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
# Helper to find a node by value
def find_node(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


# ----------------------------------------------------------------
# Test Cases
if __name__ == "__main__":
    # Test Case 1
    vals1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root1 = build_tree(vals1)
    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    print(
        "Test Case 1 Output:", lowest_common_ancestor(root1, p1, q1).val
    )  # Expected: 3

    # Test Case 2
    vals2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root2 = build_tree(vals2)
    p2 = find_node(root2, 5)
    q2 = find_node(root2, 4)
    print(
        "Test Case 2 Output:", lowest_common_ancestor(root2, p2, q2).val
    )  # Expected: 5

    # Test Case 3
    vals3 = [1, 2]
    root3 = build_tree(vals3)
    p3 = find_node(root3, 1)
    q3 = find_node(root3, 2)
    print(
        "Test Case 3 Output:", lowest_common_ancestor(root3, p3, q3).val
    )  # Expected: 1
