#Implement strStr().
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Example 1:
#Input: haystack = "hello", needle = "ll"
#Output: 2

#Example 2:
#Input: haystack = "aaaaa", needle = "bba"
#Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
