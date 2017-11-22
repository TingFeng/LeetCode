
"""

LeetCode 1: TwoSum
https://leetcode.com/problems/two-sum/description/

#Problem:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

#Solution

Use dictionary

"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    test=dict()
    for i,x in enumerate(nums):
        if target-x in test:
            return test[target-x],i
        elif x not in test:
            test[x]=i
