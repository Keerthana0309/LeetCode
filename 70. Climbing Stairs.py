#You are climbing a stair case. It takes n steps to reach to the top.Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Example 1:
#Input: 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        
        d = {1:1, 2:2}
        
        for i in range(3, n+1):
            curr = d[i-1] + d[i-2]
            d[i] = curr
        return d[n]
