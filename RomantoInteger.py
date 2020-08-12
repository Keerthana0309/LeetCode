#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
#For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.


class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {
            
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            
        }
        
        total = 0
        curr = 0
        prev = 0
        
        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr
                
            prev = curr
            
        return total   
