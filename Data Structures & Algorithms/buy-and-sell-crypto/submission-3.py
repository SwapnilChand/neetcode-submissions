import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        # prices=[1,5,6,7,1,10]
        # 4, 5, 6, 
# 0 to 7
        for i in range(len(prices) - 1):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if diff > profit:
                    profit = diff
                r += 1
            else:
                l = r
                r += 1
        return profit