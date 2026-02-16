class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        is_duplicate=False
        seen=set()
        for i in nums:
            if i in seen:
                is_duplicate=True
            seen.add(i)
            # is_duplicate=False
        return is_duplicate
sol=Solution()
num=[1,2,3,4]
print(sol.hasDuplicate(num))
