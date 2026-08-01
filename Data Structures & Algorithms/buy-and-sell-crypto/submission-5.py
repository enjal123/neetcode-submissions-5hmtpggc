class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # pick a num, compare it with another, find differen

        l, r = 0, 1
        best_profit = 0
        
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                best_profit = max(best_profit, profit)
            else:
                l = r
            
            r += 1
        
        return best_profit