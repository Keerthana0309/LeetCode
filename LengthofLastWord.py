#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.If the last word does not exist, return 0.

#Note: A word is defined as a maximal substring consisting of non-space characters only.

#Example:
#Input: "Hello World"
#Output: 5


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        return 0 if len(s) == 0 else len(s[-1])
        
