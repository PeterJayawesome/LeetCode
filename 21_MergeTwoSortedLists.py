"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2
        elif not l2:
        	return l1
        r1 = l1
        r2 = l2
        if r1.val >= r2.val:
        	newHead = r2
        	r2 = r2.next
        else:
        	newHead = r1
        	r1 = r1.next
        r = newHead
        while r1 and r2:
        	if r1.val >= r2.val:
        		r.next = r2
        		r2 = r2.next
        		r = r.next
        	else:
        		r.next = r1
        		r1 = r1.next
        		r = r.next
        if r1:
        	r.next = r1
        elif r2:
        	r.next = r2
        return newHead