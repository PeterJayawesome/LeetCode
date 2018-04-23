"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if not nums:
        	return res
        l,r = 0,len(nums)-1
        while l<r:
        	m = (l+r)/2
        	if target<nums[m]:
        		r = m
        	elif target > nums[m]:
        		l = m+1
        	else:
        		break
        if l == r:
        	return res if nums[l]!=target else [l,r]
        res = [m,m]
        while res[0]>l:
        	lm = (l+res[0])/2
        	if nums[lm]!= target:
        		l = lm+1
        	else:
        		res[0] = lm
        while res[1]<r:
        	rm=(r+res[1]+1)/2
        	if nums[rm]!=target:
        		r = rm-1
        	else:
        		res[1] = rm
        return res