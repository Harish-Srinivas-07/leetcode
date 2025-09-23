"""
Leetcode 1544 - Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
File: 1448.count_good_nodes_in_binary_tree.py

Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:



Input: root = [3,1,4,3,null,1,5]

Output: 4

Explanation: Nodes in blue are good.

Root Node (3) is always a good node.

Node 4 -> (3,4) is the maximum value in the path starting from the root.

Node 5 -> (3,4,5) is the maximum value in the path

Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]

Output: 3

Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:


Input: root = [1]

Output: 1

Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------------


def count_good_nodes_in_binary_tree(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], maxx: int) -> int:
        if not node:
            return 0

        # count good when node val is greater then prev maxx
        good = 1 if node.val >= maxx else 0

        # new ,axx pa in recursive
        new_maxx = max(maxx, node.val)

        # recursive part
        good += dfs(node.left, new_maxx)
        good += dfs(node.right, new_maxx)

        return good

    return dfs(root, root.val)


# ----------------------------------------------------------------
# Helper to build a tree from level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


# ----------------------------------------------------------------
# Test Cases
if __name__ == "__main__":
    vals1 = [3, 1, 4, 3, None, 1, 5]
    vals2 = [3, 3, None, 4, 2]
    vals3 = [1]

    root1 = build_tree(vals1)
    root2 = build_tree(vals2)
    root3 = build_tree(vals3)

    print("Output 1:", count_good_nodes_in_binary_tree(root1))  # Expected 4
    print("Output 2:", count_good_nodes_in_binary_tree(root2))  # Expected 3
    print("Output 3:", count_good_nodes_in_binary_tree(root3))  # Expected 1
