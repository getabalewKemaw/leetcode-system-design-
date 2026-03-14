class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_duplicate=False
        seen=set()
        for i in nums:
            if i in seen:
                is_duplicate=True
            seen.add(i)
        return is_duplicate
        

        