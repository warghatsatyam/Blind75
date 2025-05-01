from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    amt = [0] * (amount+1)
    for i in range(1,amount+1):
        min_count = 1000000
        for j in range(len(coins)):
            if coins[j] <= i:
                current_count = 1 + amt[i-coins[j]] 
                min_count = min (min_count, current_count)            
        amt[i] = min_count
    
    return -1 if amt[amount] == min_count else amt[amount]


def coinChangeBetterApproach(coins:List[int],amount:int) -> int:
    amt = [float('inf')] * (amount + 1)
    amt[0] = 0
    for i in range(1,amount+1):
        for c in coins:
            if c <= i:
                amt[i] = min(amt[i],1+amt[i-c])

    return -1 if amt[amount] == float('inf') else amt[amount]        
if __name__ == '__main__':
    coins = [2]
    amount = 3
    print(coinChangeBetterApproach(coins=coins,amount=amount))