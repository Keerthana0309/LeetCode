#Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

#Example 1:
#Input: 16
#Output: true

#Example 2:
#Input: 5
#Output: false


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 0:
            return False
        while num % 4 == 0:
            num //= 4
        return True if num == 1 else False
