#You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#Given n, find the total number of full staircase rows that can be formed.
#n is a non-negative integer and fits within the range of a 32-bit signed integer.

#Example 1:
#n = 5
#The coins can form the following rows:
¤
¤ ¤
¤ ¤
#Because the 3rd row is incomplete, we return 2.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l = 1
        h = n
        
        while l <= h:
            mid = l + (h - l)//2
            temp = int(mid*(mid+1)/2)
            
            if temp == n:
                return mid
            if temp < n:
                l = mid + 1
            else:
                h = mid -1
                
        return h
