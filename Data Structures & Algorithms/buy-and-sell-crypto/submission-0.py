class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_i, sell_i = 0, 0
        n = len(prices)
        while sell_i < n:
            if prices[sell_i] < prices[buy_i]:
                buy_i = sell_i
                sell_i += 1
            else:
                max_profit = max(max_profit, prices[sell_i] - prices[buy_i])
                sell_i += 1
        return max_profit