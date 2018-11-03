#!/user/bin/env python
# -*- coding: utf-8 -*-
#@Time     :2018/11/3/0003 16:10
#@Author   :zhupengfei
#@Site     :
#@File     :Leetcode-35.py
#@Software :PyCharm
#@descibe  ：
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:

输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4

示例 4:

输入: [1,3,5,6], 0
输出: 0
'''
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_insert = nums.insert
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]>target:
                nums_insert(i, target)
                return i
            else:
                if i == len(nums)-1:
                    nums_insert(i+1, target)
                    return i+1


arr = [1,3,5,7]
target = 8
cla = Solution()
cla.searchInsert(arr, target)