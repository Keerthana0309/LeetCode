#Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#For example, with A = "abcd" and B = "cdabcdab".
#Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = len(B)/len(A)
        
        if B in A * count:
            return count
        elif B in A * (count + 1):
            return count + 1
        elif B in A * (count + 2):
            return count + 2
        else:
            return -1
