class Solution(object):
    def maxProfit(self, prices):
        minbuy=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]<minbuy:
                minbuy=prices[i]
            elif prices[i]-minbuy>maxprofit:
                maxprofit=prices[i]-minbuy
        return maxprofit        



        