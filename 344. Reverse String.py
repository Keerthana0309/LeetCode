#Write a function that reverses a string. The input string is given as an array of characters char[].

#Example 1:
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s
        
