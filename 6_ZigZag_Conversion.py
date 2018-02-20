"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [""]*numRows
        a = numRows*2-2
        n = 0
        while n*a<len(s):
            m = 0
            while m<a and n*a+m < len(s):
                if m <= a/2:
                    res[m]+= s[n*a+m]
                else:
                    res[a-m] += s[n*a+m]
                m+=1
            n += 1
        return ''.join(res)