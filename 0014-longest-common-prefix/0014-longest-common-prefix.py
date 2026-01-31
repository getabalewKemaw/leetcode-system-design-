class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        if not strs:
            return ""
        
        prefix = ""
        # zip(*strs) pairs up the 1st chars, then 2nd chars, etc.
        for characters in zip(*strs):
            # If all characters in this column are the same
            if len(set(characters)) == 1:
                prefix += characters[0]
            else:
                # Mismatch found; stop immediately
                break
                
        return prefix
