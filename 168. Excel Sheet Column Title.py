#Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
#Example 1:
#Input: 1
#Output: "A"

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
	# initialize output String as empty
	res = ""

	while n > 0:

		# find index of next letter and concatenate the letter
		# to the solution

		# Here index 0 corresponds to 'A' and 25 corresponds to 'Z'
		index = (n - 1) % 26
		res += chr(index + ord('A'))
		n = (n - 1) // 26

	return res[::-1]
