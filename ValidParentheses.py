#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#1.)Open brackets must be closed by the same type of brackets.
#2.)Open brackets must be closed in the correct order.



class Solution(object):
    def isValid(self, s):
                
        stack, pairs = [], {"(":")", "{":"}", "[":"]"} 
				
        for char in s:
			# if the char is an open bracket, it'll append to our stack list
            if char in pairs:
                stack.append(char)
				
			# if the character is a closed bracket, it won't append. And if it happens that 
			# there is nothing in the list because we have an unpaired closed bracket
			# we return false
            elif len(stack) <= 0:
                return False
				
			# if the character is a closed bracket AND it's not equal to the key-value pair 
			# of the last item in the stack (remember pop takes the last item in a list), then we return false.
			# HOWEVER. If the character does match the key-value pair of the last item in stack, we have an empty stack list.
			# We continue with the for-loop until we are finished.
            elif char in pairs.values() and char != pairs[stack.pop()]:
                return False
				
		# After the for-loop our stack is empty, we succesfully matched all our brackets. 
        return True if stack == [] else False
        
