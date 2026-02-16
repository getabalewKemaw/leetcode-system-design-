class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        new_set=set(nums)
        res=[]
        for i in range(1,n+1):
            if i not in new_set:
                res.append(i)
        return res
            

