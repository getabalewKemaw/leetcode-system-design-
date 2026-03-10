class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=''.join(c for c in s if c.isalnum())

        reversed=s[::-1]
        if(reversed==s):
            return True
        else:
            return False