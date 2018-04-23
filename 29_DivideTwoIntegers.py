"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        divisor,dividend = abs(divisor),abs(dividend)
        res = 0
        while dividend >= divisor:
        	r = 1
        	c = divisor
        	while dividend >= c:
	        	res += r
	        	dividend -= c
	        	r <<= 1
	        	c <<= 1
        if res > 0x7fffffff:
        	return 0x7fffffff if positive else -0x80000000
        return res if positive else -res