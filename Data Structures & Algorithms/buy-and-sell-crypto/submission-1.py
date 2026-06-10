class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        i = 0
        j = 0

        while(j<=len(prices)-1):
            if prices[i] > prices[j]:
                i = j 
            
            else:
                profit = max(profit, prices[j] - prices[i])
            j +=1
            
        return profit


        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             margin = prices[j] - prices[i]

        #             if margin > profit :
        #                 profit = margin
        # return profit


                
        