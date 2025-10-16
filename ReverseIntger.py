# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self,x):

        # trying to understand the problem  first
        # reverse the number and when it reverse if 0  go outside  and if negative  still the negative is not reversed  that means the sign is not reversed 
        sign=1 if x>0 else -1
        x=abs(x)
        reversed=int(str(x)[::-1])
        #[-231, 231 - 1] make these do and if true return 0
        reversed*=sign
        if(reversed<(-2**31)) or (reversed>(2**31)-1):
            return 0
        return reversed


s=Solution()
print(s.reverse(-120))
         #make the x absoluet values so later on we multiply bythat and retunr the sign
         


class Solution2(object):
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            if str(x)==str(x)[::-1]:
             return True
            return False
          
h=Solution2()
print(h.isPalindrome(-121))  