#!/user/bin/env python
# -*- coding: utf-8 -*-
#@Time     :2018/11/30/0030 16:56
#@Author   :zhupengfei
#@Site     :
#@File     :bubbsort.py
#@Software :PyCharm
#@descibe  ：算法思想
'''
冒泡排序要对一个列表多次重复遍历。它要比较相邻的两项，并且交换顺序排错的项。每对 列表实行一次遍历，就有一个最大项排在了正确的位置。大体上讲，列表的每一个数据项都会在 其相应的位置 “冒泡”。如果列表有 n 项，第一次遍历就要比较 n-1 对数据。需要注意，一旦列 表中最大(按照规定的原则定义大小)的数据是所比较的数据对中的一个，它就会沿着列表一直 后移，直到这次遍历结束。

'''
#自己理解：主要是两个循环，第一个大循环控制的是还没有排序好的（排除掉已经排好的大的值，都在最后了），因为冒泡排序是两两对比，把对比过程中最大的放到最后去，就是说第一次大循环
#找出的是最大的，然后剩下的再来一次两两比较，第二次大循环找出次大的，以此类推

import time

#构造一个计算函数运行时间的装饰器，对比优化后函数的运行时间提高了多少
def timecout():
	def decorator(func):
		def wrapper(*args, **kwargs):
			start = time.time()
			l = func(*args, **kwargs)
			end = time.time()
			t = end - start
			print('time is : %s'%t)
			return l
		return wrapper
	return decorator

@timecout()
def bubbSort(list):
	size = len(list)
	for i in range(size-1, 0, -1):
		for j in range(0, i):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list
list = [2,4, 1, 5, 7, 3, 9]
list_new = bubbSort(list)
print(list_new)

#优化思路：可以调试上面代码发现，如果内循环中两两比较没有交换位置的这个过程了，那么就说明数组已经排好了，就可以结束后面的不必要循环了
@timecout()
def bubbSort_new(list):
	size = len(list)
	NoRev = False
	for i in range(size-1, 0, -1):
		for j in range(0, i):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
				NoRev = False
		if NoRev == True:
			break
	return list
list = [2,4, 1, 5, 7, 3, 9]
list_new1 = bubbSort_new(list)
print(list_new1)