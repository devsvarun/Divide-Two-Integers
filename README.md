# Divide-Two-Integers

This program divides two integers without using divide, multiply and mod operator.

Algorithm:
1. While absolute of dividend is greater than or equal to divisor.
  1.1 - Check the difference between the absolute dividend and the absolute divisor shifted left for a number of "times" (initially zero).
  1.2 - If the difference is greater than or equal to zero.
    1.2.1 - Left shift 1 for a number of "times" and add that value to the "quotient".
    1.2.2 - Increase the value of "times" by one.
    1.2.3 - Set the current differnce as the new dividend.
  1.3 - Else set the value of times equal to zero to reset the "times" to its initial value.
2. Return quotient according to the upper and lower limit.
