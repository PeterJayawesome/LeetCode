"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = ["{}",'()','[]']
        openset = '[({'
        closeset = ']})'
        for letter in s:
            if letter in openset:
                stack.append(letter)
            if letter in closeset:
                if not stack or (stack.pop()+letter) not in pairs:
                    return False
        return len(stack) == 0