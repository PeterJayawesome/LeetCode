"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        NToS = {'2':['a','b','c'],'9':['w','x','y','z'],
                '3':['d','e','f'],'4':['g','h','i'],
                '5':['j','k','l'],'6':['m','n','o'],
                '7':['p','q','r','s'],'8':['t','u','v']}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return NToS[digits]
        res = self.letterCombinations(digits[:-1])
        return [s+a for s in res for a in NToS[digits[-1]]]