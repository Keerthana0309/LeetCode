#Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

#Example 1:
#Input: "abab"
#Output: True
#Explanation: It's the substring "ab" twice.

#Example 2:
#Input: "aba"
#Output: False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        return s in (s + s)[1: -1]
