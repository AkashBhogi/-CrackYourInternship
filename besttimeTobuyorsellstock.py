class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0;r=1;m=0;n=len(prices)
        while r<n:
            c=prices[r]-prices[l]
            if prices[r]>prices[l]:
                m=max(c,m)
            else:
                l=r
            r+=1
        return m
