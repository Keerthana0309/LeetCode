#Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

#Example 1:
#Input: 5
#Output: True
#Explanation: 1 * 1 + 2 * 2 = 5
 
#Example 2:
#Input: 3
#Output: False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        low = 0
        high = int(math.sqrt(c))
        while low <= high:
            sum = low**2 + high**2
            if sum < c:
                low += 1
            if sum > c:
                high -= 1
            if sum == c:
                return True
        return False
