#!-*- coding:utf-8 -*-
# author:zhupengfei
# datetime:2018/11/22 20:03
# software:PyCharm
# discribe:给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # L = len(digits)
        # digits[L-1]+=1
        # return digits

        #这里把carry当做进一位，传送，很关键
        carry = 1
        #倒着循环
        for i in range(0, len(digits))[::-1]:
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                #有进一位，所以carry还是1，如果没有进一位，carry置零，后面的循环就不加了
                carry = 1
            else:
                carry = 0
        #如果list第一位加了还有进一位，那么在第一位插入1
        if carry > 0:
            digits.insert(0, 1)
        return digits

a = Solution()
digits = [1,8,9]
b = a.plusOne(digits)
print(b)
