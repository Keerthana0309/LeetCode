#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Example 1:
#Input: "A man, a plan, a canal: Panama"
#Output: true

#Example 2:
#Input: "race a car"
#Output: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        return s == s[::-1]
        
