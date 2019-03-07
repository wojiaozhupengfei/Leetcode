class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        for i in nums:
            if i in s.keys():
                s.pop(i)
            else:
                s[i] = "any"
        return list(s.keys())[0]