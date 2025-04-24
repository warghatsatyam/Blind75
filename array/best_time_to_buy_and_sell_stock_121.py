from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    for price in prices[1:]:
        if buy < price:
            current_profit = price - buy
            profit = max(profit,current_profit)
        else:
            buy = price
    return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    profit = maxProfit(prices=prices)    
    print(profit)