class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
   
        res = []
        nums.sort()  # Step 1: Sorting is crucial for two pointers and duplicate skipping

        for i, a in enumerate(nums):
            # Step 2: Skip the same value for the 'anchor' number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Optimization: If the first number is > 0, the sum will always be > 0
            if a > 0:
                break

            # Step 3: Two-pointer search for the remaining two numbers
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1  # Sum too large, move right pointer left
                elif three_sum < 0:
                    l += 1  # Sum too small, move left pointer right
                else:
                    # Sum is exactly 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second number to ensure unique triplets
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
