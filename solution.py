class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        self.dividend = abs(dividend)
        self.divisor = abs(divisor)
        quotient, times = 0,0
        upper_limit = 2**31 - 1
        lower_limit = -2**31
        while(self.dividend >= self.divisor):
            current = self.dividend - (self.divisor << times)
            if current >= 0:
                quotient += (1 << times)
                times += 1
                self.dividend = current
            elif current < 0:
                times = 0
        if(dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            quotient *= -1
            return max(quotient, lower_limit)
        return min(quotient, upper_limit)

div = Solution()
dividend = 2417483647
divisor = 2
quotient = div.divide(dividend, divisor)
print(quotient)



