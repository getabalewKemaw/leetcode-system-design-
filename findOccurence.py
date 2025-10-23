class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

# Test
s = Solution()
print(s.strStr("sadbutsad", "sad"))   # Output: 0
print(s.strStr("leetcode", "leeto"))  # Output: -1
