#Given a positive integer num, write a function which returns True if num is a perfect square else False.

#Example 1:
#Input: num = 16
#Output: true

#Example 2:
#Input: num = 14
#Output: false


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 1
        right = num
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid*mid
            
            if square < num:
                left = mid +1
            elif square > num:
                right = mid -1
            else:
                return True
            
        return False
