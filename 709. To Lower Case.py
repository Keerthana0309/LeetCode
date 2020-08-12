#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

#Example 1:
#Input: "Hello"
#Output: "hello"

#Example 2:
#Input: "here"
#Output: "here"

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower = ""
        for i in range(len(str)):
            a = ord(str[i])
            if a >= 65 and a <= 90:
                lower+=chr(a+32)
            else:
                lower+=chr(a)
        return lower
        
