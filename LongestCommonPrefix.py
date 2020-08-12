#Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".
#Example 1:
#Input: ["flower","flow","flight"]
#Output: "fl"

#Example 2:
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings


class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        shortest_str = min(strs,key=len)
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str
