class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        m_min = prices[0]
        m_max = 0
        for i in prices:
            m_min = min(m_min, i)
            m_max = max(m_max, i - m_min)
        return m_max