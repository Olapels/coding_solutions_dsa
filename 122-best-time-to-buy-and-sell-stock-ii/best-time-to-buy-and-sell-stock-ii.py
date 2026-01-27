class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy,sell = 0,1

        for sell in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                profit += prices[sell] - prices[buy]
            prices[buy] = prices[sell]
        
        return profit
        