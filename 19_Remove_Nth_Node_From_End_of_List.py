"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        r1 = head
        while r1:
        	r1 = r1.next
        	i += 1
       	if i == n:
       		head = head.next
       		return head
        r2 = head
        j = 0
        while r2.next and j<i-n-1:
        	r2 = r2.next
        	j += 1
        r2.next = r2.next.next
        return head