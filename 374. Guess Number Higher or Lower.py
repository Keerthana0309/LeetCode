#We are playing the Guess Game. The game is as follows:I pick a number from 1 to n. You have to guess which number I picked.
#Every time you guess wrong, I'll tell you whether the number is higher or lower.
#You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

#-1 : My number is lower
# 1 : My number is higher
# 0 : Congrats! You got it!

#Example :
#Input: n = 10, pick = 6
#Output: 6

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower , upper = 1, n 
        
        while lower <= upper:
            
            mid = lower + (upper-lower)//2
            
            query = guess(mid)
            if query == 0:
                return mid
            
            elif query == 1:
                lower = mid + 1
                
            else:
                upper = mid - 1
        
