#Given an integer n, return the number of trailing zeroes in n!.

#Example 1:
#Input: 3
#Output: 0
#Explanation: 3! = 6, no trailing zero.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n / 5
            count += n
        return count
