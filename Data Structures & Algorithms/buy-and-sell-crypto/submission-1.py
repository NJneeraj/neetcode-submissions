class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,profit= prices[0],0
        # index = 0   1    2   3   4   5  6
        # buy   = 10  1    1   1        
        # profit= 0   0    4    5
    # price-buy = -9  4     5
        for i in range(1,len(prices)):
            price = prices[i]
            if price-buy > profit:
                profit = price-buy
            if price < buy :
                buy= price
        return profit
            