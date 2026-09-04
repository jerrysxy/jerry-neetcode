class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest_profit = 0
        cheapest = prices[0]

        for price in prices:
            if price < cheapest:
                cheapest = price
            
            profit = price - cheapest
            if profit > biggest_profit:
                biggest_profit = profit
        return biggest_profit
