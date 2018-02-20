def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    s1 = 0
    s2 = 0
    negsum = 0
    for num in nums:
        if num < 0:
            if s1 > 0 and s2 > 0:
                if s1+negsum >= 0 and s2+negsum >=0:
                    s1 += negsum+s2
                    s2 = 0
                    negsum = num
                elif s1+negsum >= 0:
                    negsum += s2+num
                    s2 = 0
                else:
                    if s1 > res:
                        res = s1
                    s1 = s2
                    s2 = 0
                    negsum = num
            elif s1>0:
                negsum += num
        elif negsum < 0:
            s2 += num
        else:
            s1 += num
        print num,s1,s2,negsum
    return max(res,s1,s2,s1+s2+negsum) if s1 else max(arr)



arr = [1,2]
print maxSubArray(arr)