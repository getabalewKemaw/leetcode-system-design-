class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=0
        current_streak=0
        for num in nums:
            if num==1:
               current_streak+=1
               if current_streak>largest:
                largest=current_streak
            else:
                current_streak=0
        return largest


                 
 