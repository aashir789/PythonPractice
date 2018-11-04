'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
        def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x >= pow(2, 31) or x < pow(-2, 31):
                return 0
        elif x > 0:
                original = x
        else:
                original = -1 * x
        new_number = 0
        while original > 0:
                remainder = original % 10
                original = original/10
                new_number = new_number * 10 + remainder
                        
        if new_number >= pow(2, 31) or new_number < pow(-2, 31):
                return 0
        return new_number if x > 0 else -1 * new_number
                
