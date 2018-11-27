#!-*- coding:utf-8 -*-
# author:zhupengfei
# datetime:2018/11/26 19:24
# software:PyCharm
# discribe:实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。



#次奥    我不会写了  麻蛋，下面的程序是错的

#二分法
class Sulotion:
    def mySqrt(self, a):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        mid, pre = 0, 1
        low, high = 0, x
        mid = (low + high)/2
        while(abs(mid - pre) > 0.0000001):
            if(mid*mid > x):
                high = mid
            else:
                low = mid
            pre = mid
            mid = (low+high)/2
        return int(mid)

x= 8
a = Sulotion()
ret = a.mySqrt(x)
print(ret)
