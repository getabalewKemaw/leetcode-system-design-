class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #first sort the array.
        nums.sort()
        #set sample sum first
        closest_sum=nums[0]+nums[1]+nums[2]
        n=len(nums)
        for i in range(n-2):
            left=i+1
            right=n-1
            while left < right:
                current_sum=nums[i]+nums[left]+nums[right]
                #then update the closest sum depend on comparison with the sum first we store
                if abs(current_sum-target) < abs(closest_sum-target):
                    closest_sum=current_sum
                #then we move the pointer to iterate
                if  current_sum <target:
                    left +=1
                elif current_sum>target:
                    right -=1
                else:
                    #exact sum
                    return current_sum
        return closest_sum