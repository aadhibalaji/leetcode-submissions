class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        left = 0
        right = 0

        while right < len(prices) - 1:
            right += 1
            profit = max(profit, (prices[right] - prices[left]))

            if prices[right] < prices[left]:
                left = right

        
        return profit
