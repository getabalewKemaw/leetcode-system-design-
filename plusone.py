class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry over
        
        # If all digits were 9
        return [1] + digits

# Examples
s = Solution()
print(s.plusOne([1,2,3]))  # Output: [1,2,4]
print(s.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(s.plusOne([9]))  # Output: [1,0]
print(s.plusOne([9,9,9]))  # Output: [1,0,0,0]
