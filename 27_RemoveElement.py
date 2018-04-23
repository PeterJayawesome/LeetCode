"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    	j = len(nums)-1
    	while j >= 0 and nums[j] == val:
    		j -= 1
    	i = 0
    	while i <= j:
    		if nums[i] == val:
    			nums[i] = nums[j]
    			j -= 1
    			while nums[j]==val:
    				j -= 1
    		i += 1
    	return i