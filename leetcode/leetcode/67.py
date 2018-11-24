#!-*- coding:utf-8 -*-
# author:zhupengfei
# datetime:2018/11/23 18:23
# software:PyCharm
# discribe:给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"

def Binary2Decimal(a):
    '''

    :param a: str
    :return:
    '''
    sum = 0
    for i in range(len(a)):
        sum+=2**i
    return sum
def Decimal2Binary(a):
    '''

    :param a: int
    :return:
    '''
    binary = ''
    while(a != 0):
        b = str(a%2)
        # binary.insert(0, b)
        binary+=b
        a = int(a/2)
    binary = binary[::-1]
    return binary

class Sulotion:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # sum = Binary2Decimal(a) + Binary2Decimal(b)
        # ret = Decimal2Binary(sum)
        # return ret

        # res = ''
        # i, j, plus = len(a) - 1, len(b) - 1, 0
        # while i >= 0 or j >= 0 or plus == 1:
        #     plus += int(a[i]) if i >= 0 else 0
        #     plus += int(b[j]) if j >= 0 else 0
        #     res = str(plus % 2) + res
        #     i, j, plus = i - 1, j - 1, plus / 2
        # return res

# a = '111'
# b = 11
# sum = Binary2Decimal(a)
# binary = Decimal2Binary(b)
# print(binary)
# print(sum)
a = '11'
b = '1'
c = Sulotion()
ret = c.addBinary(a, b)
print(ret)