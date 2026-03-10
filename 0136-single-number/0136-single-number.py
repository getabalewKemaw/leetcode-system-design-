class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        for i in s:
            if nums.count(i)==1:
                return i

        
