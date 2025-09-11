"""
Leetcode 2216 - Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
File: 2095.delete_the_middle_node_of_a_linked_list.py

Difficulty: Medium
Tags: Linked List, Two Pointers

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105


"""


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:

        # edge: one node or no node
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # fast by 2 , slow by 1
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # now fast at end: slow at middle -> delete
        prev.next = slow.next

        return head


"""
HINT
1. solution one to get length of ll -> delete length//2 element (easy not rec)
2. solution two pass -> slow, fast (2X steps) -> when fast reach end : slow at middle
"""


# TEST CASES ------

# Example 1
nums = [1, 3, 4, 7, 1, 2, 6]
head = build_linked_list(nums)
res = Solution().deleteMiddle(head)
print(linked_list_to_list(res))  # [1,3,4,1,2,6]

# Example 2
nums = [1, 2, 3, 4]
head = build_linked_list(nums)
res = Solution().deleteMiddle(head)
print(linked_list_to_list(res))  # [1,2,4]

# Example 3
nums = [2, 1]
head = build_linked_list(nums)
res = Solution().deleteMiddle(head)
print(linked_list_to_list(res))  # [2]

# Example 4 (edge case: one node)
nums = [10]
head = build_linked_list(nums)
res = Solution().deleteMiddle(head)
print(linked_list_to_list(res))  # []
