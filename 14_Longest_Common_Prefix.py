"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs,key=len)
        for i,s in enumerate(shortest):
            for other in strs:
                if other[i] != s:
                    return shortest[:i]
        return shortest