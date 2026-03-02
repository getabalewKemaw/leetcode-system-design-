class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # then find the start of the duplicate (so that is the Val of dupl..)
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        
        

