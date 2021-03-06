#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.


#Example:
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s==target:
                return [l+1,r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
