class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        start = 0
        end = 0

        # Helper function to expand around center
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome

        for i in range(len(s)):
            # Odd length palindrome
            len1 = expandAroundCenter(i, i)
            # Even length palindrome
            len2 = expandAroundCenter(i, i + 1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start:end + 1]
