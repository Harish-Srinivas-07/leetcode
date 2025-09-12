"""
Leetcode 206 - Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
File: 206.reverse_linked_list.py

Difficulty: Easy
Tags: Linked List, Recursion

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:


Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ITERATIVE solution
def reverse_list_iterative(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next  # save next
        current.next = prev  # reverse link
        prev = current  # move prev forward
        current = next_node  # move current forward
    return prev


# ----------------


# RECURSIVE solution
def reverse_list_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)

    # main swap & pointer change
    head.next.next = head  # 2-> 3-> None : 3-> 2-> 3-> None
    head.next = None  # 3-> 2-> None

    return new_head


# ----------------
# Helper function to convert list to linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    # Example input
    input_list = [1, 2, 3, 4, 5]
    head = list_to_linked_list(input_list)

    # Choose solution:
    # reversed_head = reverse_list_iterative(head)
    reversed_head = reverse_list_recursive(head)

    # Convert back to list to print
    output_list = linked_list_to_list(reversed_head)
    print("Output:", output_list)
