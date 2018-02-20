"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        temp = ListNode(0)
        temp.next = head
        r = temp
        while r.next and r.next.next:
        	t = r.next
        	r.next = r.next.next
        	t.next = r.next.next
        	r.next.next = t
        	r = r.next.next
        return temp.next