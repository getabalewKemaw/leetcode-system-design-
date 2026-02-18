class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #  detect the first and check for the corresponding others
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack=[]
        for char in s:
            if char in bracket_map:
                top_ele=stack.pop() if stack else "#"
                if bracket_map[char]!=top_ele:
                    return False 
            else:
                stack.append(char)
        return not stack

