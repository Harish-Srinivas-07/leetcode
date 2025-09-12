"""
Leetcode 328 - Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
File: 328.odd_even_linked_list.py

Difficulty: Medium
Tags: Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # store even for fina merge

        while even and even.next:
            odd.next = even.next  # link with next odd node
            odd = odd.next  # change pointer

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


# Helper function to build linked list from Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Example usage
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    head = build_linked_list(input_list)
    solution = Solution()
    new_head = solution.oddEvenList(head)
    output_list = linked_list_to_list(new_head)
    print("Output:", output_list)
