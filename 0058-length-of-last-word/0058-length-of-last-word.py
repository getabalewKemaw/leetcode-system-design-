class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #  here is how to to solve first scan for spaces in the word and see 
        #  see the last space and then we count the word that is bove those
        # fisrt split the word
        res=s.split()
        return len(res[-1])


        