class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total=0
        for i in range(len(s)):
            # get the first values fisrt
            value=roman[s[i]]
            #check for if it has next symbol and compare ut
            if i + 1 <len(s) and value < roman[s[i+1]]:
                total-=value
            else:
                total+=value
        return total