class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_returns = 0

        for i in range (len(prices)-1):
            if prices[i+1] > prices[i]: max_returns += prices[i+1] - prices[i]
            
        return max_returns