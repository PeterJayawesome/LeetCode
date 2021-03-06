"""
Given n non-negative integers a1, a2, ..., an, where each 
represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai) 
and (i, 0). Find two lines, which together with x-axis forms 
a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height)-1
        while i < j:
            if res < (j-i)*min(height[i],height[j]):
                res = (j-i)*min(height[i],height[j])
            if height[j] < height[i]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1
                i += 1
        return res