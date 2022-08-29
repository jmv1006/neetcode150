def maxProfit(prices):
    profits = {}

    p1 = 0
    p2 = len(prices) - 1
    
    while(p1 < p2):
        if(prices[p2] > prices[p1]): ##profitable
            profit = prices[p2] - prices[p1]
            profits[profit] = 0
            p2 -= 1
        else:
            p1 += 1
    
    if profits: return max(profits) 
    else: return 0


prices = [7,6,4,3,1]
print(maxProfit(prices))