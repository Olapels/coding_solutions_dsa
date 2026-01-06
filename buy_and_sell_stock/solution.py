from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #edge case if list is empty
        if not prices:
            return 0
    
        buy,sell=0,1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
            else:
                #found a cheaper price to buy
                buy=sell
            sell+=1
        
        return max_profit