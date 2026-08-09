class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # pick a num, compare it with another, find differen

        l, r = 0, 1
        best_profit = 0
        
        while r < len(prices):

            if prices[r] > prices[l]:
                print(prices[r])
                print(prices[l])
                profit = prices[r] - prices[l]
                print(profit)
                best_profit = max(best_profit, profit)
            else:
                l = r

            r+=1

        return best_profit