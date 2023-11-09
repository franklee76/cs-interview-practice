class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_return = 0

        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if prices[i] - min_price > max_return:
                max_return = prices[i] - min_price

        return max_return