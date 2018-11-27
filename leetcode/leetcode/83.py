#!-*- coding:utf-8 -*-
# author:zhupengfei
# datetime:2018/11/27 19:22
# software:PyCharm
# discribe:给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while(p):
            if p.next and p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
