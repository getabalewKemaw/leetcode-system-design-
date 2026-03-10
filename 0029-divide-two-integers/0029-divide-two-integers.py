class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # double the divisor and the count (multiple) 
            # until it's just under the remaining dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # subtract the largest chunk we found from the dividend
            dividend -= temp_divisor
            # add how many times the divisor went into that chunk
            quotient += multiple
            
        # 5. apply the sign and return within 32-bit bounds
        if negative:
            quotient = -quotient
            
        return max(MIN_INT, min(MAX_INT, quotient))
