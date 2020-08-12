#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

#F(0) = 0,   F(1) = 1
#F(N) = F(N - 1) + F(N - 2), for N > 1.
#Given N, calculate F(N).

#Example 1:
#Input: 2
#Output: 1
#Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

class Solution:
    def fib(self, N: int) -> int:
        
        dict = {}
        
        dict[0] = 0
        dict[1] = 1
        
        for n in range(2, N+1):
            dict[n] = dict[n-1] + dict[n-2]
        return dict[N]
        