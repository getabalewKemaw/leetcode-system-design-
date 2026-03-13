class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        max_freq = 0
        ans = -1
        for num in nums:
            if num % 2 == 0: 
                counts[num] = counts.get(num, 0) + 1
                freq = counts[num]
                if freq > max_freq:
                    max_freq = freq
                    ans = num
                elif freq == max_freq:
                    ans = min(ans, num)

        return ans