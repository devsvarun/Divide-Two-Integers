class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        self.dividend = abs(dividend)  # abslolute of the "dividend"
        self.divisor = abs(divisor)  # abslolute of the "divisor"
        quotient, times = 0,0  # "quotient" is the main output if it is in between the upper and lower limit
                               # "times" is the number of times we shift left
        upper_limit = 2**31 - 1  # upper limit of the "quotient"
        lower_limit = -2**31  # lower limit of the "quotient"
        while(self.dividend >= self.divisor):
            current = self.dividend - (self.divisor << times)  # "current" is current difference between the "self.dividend" 
                                                               # and "self.divisor" shifted left for the set number of "times"
            if current >= 0:
                quotient += (1 << times)  # left shift 1 for the set number of "times" and add that to the quotient
                times += 1
                self.dividend = current
            elif current < 0:
                times = 0  # if current is less than zero, that means we are close to the value of our dividend
                           # so, reset the value of times
                    
        if(dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):  # handling the negative integers
            quotient *= -1
            return max(quotient, lower_limit)  # return according to the lower limit
        return min(quotient, upper_limit)  # return according to the upper limit

div = Solution()
dividend = 2417483647
divisor = 2
quotient = div.divide(dividend, divisor)
print(quotient)



