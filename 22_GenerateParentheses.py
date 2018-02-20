"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generater(p,l,r,res=[]):
        	if l:
        		generater(p+'(',l-1,r)
        	if r>l:
        		generater(p+')',l,r-1)
        	if not r:
        		res.append(p)
        	return res
        return generater('',n,n)