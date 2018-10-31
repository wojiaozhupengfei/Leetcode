#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29/0029 8:56
# @Author  : zhupengfei
# @Site    : 
# @File    : Leetcode-20.py
# @Software: PyCharm

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true
'''

class Solution:
    def isValid(self, s):
        #定义符号表
        dict = {')': '(', '}': '{', ']': '['}
        #左右符号分开
        dict_L, dict_R = dict.values(), dict.keys()
        result = []
        #加速
        reuslt_append = result.append
        reuslt_pop = result.pop
        if len(s)%2 == 1 or s == None:
            return False
        #遍历s的符号
        for i in s:
            #如果符号在左符号表中，那么就入栈
            if i in dict_L:
                reuslt_append(i)
            #如果符号在右符号表中，那么就该进行匹配了，能匹配到就返回true，否则返回false
            elif i in dict_R:
                if result and result[-1] == dict[i]:
                    reuslt_pop()

                else:
                    return False
        return len(result) == 0

s = '(()('
a = Solution()
a.isValid(s)