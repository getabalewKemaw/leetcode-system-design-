class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicated_num=0
        n=len(nums)
        seen=set()
        res=[]
        for x in nums:
            if x in seen:
                 duplicated_num=x
            seen.add(x)
                 
        #  getting the missing nums as well
        missing=-1
        for i in range(1,n+1):
            if i  not in seen:
                missing=i
        return [duplicated_num,missing]
                
                
        
        

        