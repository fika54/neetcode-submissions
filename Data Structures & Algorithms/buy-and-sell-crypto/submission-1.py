class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        l = 0
        r = len(prices) - 1

        bestBuy = prices[l]
        bestSell = prices[r]


        while l < r:

            if bestBuy > prices[l]:
                bestBuy = prices[l]

            if bestSell < prices[r]:
                bestSell = prices[r]

            rProf = prices[r-1] - bestBuy
            lProf = bestSell - prices[l+1]

            if rProf > lProf:
                r -= 1
            else:
                l += 1
        
        profit = bestSell - bestBuy
        
        return max(profit, 0)

            


        