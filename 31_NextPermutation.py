"""
Implement next permutation, which rearranges numbers into the lexicographically next greater 
permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order 
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs 
are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

"""
Well, in fact the problem of next permutation has been studied long ago. From the Wikipedia page,
in the 14th century, a man named Narayana Pandita gives the following classic and yet quite 
simple algorithm (with minor modifications in notations to fit the problem statement):

1)Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, the permutation 
is sorted in descending order, just reverse it to ascending order and we are done. For example, 
the next permutation of [3, 2, 1] is [1, 2, 3].
2)Find the largest index l greater than k such that nums[k] < nums[l].
3)Swap the value of nums[k] with that of nums[l].
4)Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1].

Quite simple, yeah? Now comes the following code, which is barely a translation.

Well, a final note here, the above algorithm is indeed powerful — it can handle the cases of 
duplicates! If you have tried the problems Permutations and Permutations II, then the following 
function is also useful. Both of Permutations and Permutations II can be solved easily using this 
function. Hints: sort nums in ascending order, add it to the result of all permutations and then 
repeatedly generate the next permutation and add it … until we get back to the original sorted 
condition. If you want to learn more, please visit this solution and that solution.
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                k = i
                break
        if k ==-1:
            nums.reverse()
            return
        l = len(nums)-1
        for j in xrange(len(nums)-1,-1,-1):
            if nums[j]>nums[k]:
                l = j
                break
        t = nums[k]
        nums[k] = nums[l]
        nums[l] = t
        nums[k+1:] = nums[k+1:][::-1]
        return