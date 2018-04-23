"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
        	return -1
        if target == nums[-1]:
        	return len(nums)-1
        l,r = 0,len(nums)-1
        while l<r:
        	m = (l+r)/2
        	if target > nums[m]:
        		if nums[m]>nums[-1] or target<nums[-1]:
        			l = m+1
        		else:
        			r = m
        	elif target<nums[m]:
        		if nums[m]<nums[-1] or target>nums[-1]:
        			r = m
        		else:
        			l = m+1
        	else:
        		return m
        return l if nums[l]==target else -1