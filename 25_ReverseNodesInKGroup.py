"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = link = ListNode(0)
        dummy.next = r = l = head
        while true:
        	count = 0
        	while r and count < k:
        		r = r.next
        		count += 1
        	if count == k:
        		pre,cur = r,l
        		for i in xrange(k):
        			cur.next,cur,pre = pre,cur.next,cur
        		link.next,link,l = pre,l,r
        	else:
        		return dummy.next