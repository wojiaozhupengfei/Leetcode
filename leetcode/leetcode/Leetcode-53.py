#!/user/bin/env python
# -*- coding: utf-8 -*-
#@Time     :2018/11/7/0007 19:50
#@Author   :zhupengfei
#@Site     :
#@File     :Leetcode-53.py
#@Software :PyCharm
#@descibe  ：
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

'''
解题思路：从前面的子串开始，与当前的单个值比较，取大的，用这个大的值替换nums数组中的当前值，然后进行下一步循环，最后nums数组中就存了子串和最大的值
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1, length):
            #nums[i]取值为两者之间大的
            nums[i] = max(nums[i] + nums[i -1], nums[i])
        return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
c = Solution()
d = c.maxSubArray(nums)
print(d)