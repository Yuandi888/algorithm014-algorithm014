# 122. Best Time to Buy and Sell Stock II
# 122. 买卖股票的最佳时机 II



# 采用贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                all += prices[i+1] - prices[i]
        return all


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/yi-xing-dai-ma-xing-neng-da-dao-100-by-jamleon/
# 速度最快，prices[i] - prices[i-1] > 0 比 prices[i] > prices[i-1] 快
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] - prices[i-1] > 0)



# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/122mai-mai-gu-piao-de-zui-jia-shi-ji-ii-pythonyi-x/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(x-y for x, y in zip(prices[1:], prices) if x-y > 0)