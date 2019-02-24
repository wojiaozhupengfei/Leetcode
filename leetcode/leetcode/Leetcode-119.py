#!/user/bin/env python
# -*- coding: utf-8 -*-
#@Time     :2019/2/24/0024 16:45
#@Author   :zhupengfei
#@Site     :
#@File     :Leetcode-119.py
#@Software :PyCharm
#@descibe  ：

# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
# 我们来模拟下：
# 0，【1】
# 1，【1,1】
# 2，【1,2,1】
# 3，【1,3,3,1】
# 即第i行和第i-1行的关系为
# a[i][j] = a[i-1][j-1] + a[i-1][j] 。开头和结尾处为1。不用计算。

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if not rowIndex:
	        return row
        for i in range(rowIndex):
	        #这里和C++的写法不同之处在于C++是row[j-1]+row[j]是因为
	        row = [1] + [row[j +1] + row[j] for j in range(len(row) - 1)] + [1]
        return row