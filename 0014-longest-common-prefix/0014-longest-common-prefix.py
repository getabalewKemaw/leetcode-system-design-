class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        
        
        if not strs:
          return ""
        prefix=""
        for characters in zip(*strs):

        #   check  if the corresponding letter are the same or not 
            if(len(set(characters))==1):
              prefix +=characters[0]
            else:
                 break
        return prefix