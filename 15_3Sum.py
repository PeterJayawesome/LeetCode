"""
Given an array S of n integers, are there elements a, b, 
c in S such that a + b + c = 0? Find all unique triplets in 
the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    counter = {} 
    for num in nums:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1

    if 0 in counter and counter[0] > 2:
        rst = [[0, 0, 0]]
    else:
        rst = []

    uniques = counter.keys() #它使用hash table来过滤重复数字

    pos = sorted(p for p in uniques if p > 0) #我只利用了将数组排列这一特征
    neg = sorted(n for n in uniques if n < 0)
    
    #我也采取了分组(正数和负数)这一特征
    for p in pos:
        for n in neg:
            inverse = -(p + n) #通过设置sub-goal来设置
            if inverse in counter:
                if inverse == p and counter[p] > 1:
                    rst.append([n, p, p])
                elif inverse == n and counter[n] > 1:
                    rst.append([n, n, p])
                elif (not n <= inverse <= p) or inverse == 0:
                    rst.append([n, inverse, p])
    return rst