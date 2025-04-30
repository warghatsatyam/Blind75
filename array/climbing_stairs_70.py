
#Approach 1 This takes two much time TC is (2^n)
from functools import lru_cache


def climbStairsApproachOne(n: int) -> int:
    if n == 1:
        return 1 
    if n == 2:
        return 2 
    
    return climbStairsApproachOne(n-1) + climbStairsApproachOne(n-2)


#Approach 2 we store the result of previous computation

@lru_cache(None)
def climbStairsApproachTwo(n: int) -> int:
    if n == 1:
        return 1 
    if n == 2:
        return 2 
    
    return climbStairsApproachTwo(n-1) + climbStairsApproachTwo(n-2)

#Approach 3 we using iterative approach 


def climbStairsApproachThree(n:int) -> int:
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b



if __name__ == '__main__':
    number_of_ways = climbStairsApproachThree(n=3)
    print(number_of_ways)