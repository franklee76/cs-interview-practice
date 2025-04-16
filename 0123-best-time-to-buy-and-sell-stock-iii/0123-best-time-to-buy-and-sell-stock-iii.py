class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        for price in prices:
            # Update first buy: min of previous buy or buying today
            buy1 = min(buy1, price)
            # Update first sell: max of previous sell or selling today
            sell1 = max(sell1, price - buy1)
            # Update second buy: min of previous buy or buying today after first sell
            buy2 = min(buy2, price - sell1)
            # Update second sell: max of previous sell or selling today
            sell2 = max(sell2, price - buy2)
        
        return sell2

