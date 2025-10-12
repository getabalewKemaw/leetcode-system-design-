# #  day 1  

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# brute force method of finding using nested loop timecomplexity is o(n^2)
class Solution:
    def two_sum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return([i,j])
                
my_solution=Solution()
result=my_solution.two_sum([2,7,11,15],9)
print(f"the result is {result}")

# but the time complexity is o(n^2)
# so how to make that efficient?

# using the hash map or dictionary structure

# Use a dictionary to remember numbers we have seen and their indices.
# For each number num at index i, check if target - num exists in the dictionary.
# If yes → we found the pair.
# Otherwise → store num in the dictionary
class Solution2:
          def twoSum(self, nums, target):
            num_map = {}  # key: number, value: index
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_map:
                    return [num_map[complement], i]
                num_map[num] = i
solution_instance = Solution2()
result=solution_instance.twoSum([2,7,11,15],9)
print(result)
# so yeap that is order of 1