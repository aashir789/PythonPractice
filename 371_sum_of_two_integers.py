'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

https://leetcode.com/problems/sum-of-two-integers/description/
'''
class Solution(object):
        def getSum(self, a, b):
                    """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0: return a
        carry = (a & b)<< 1
        sum = a ^ b
        while carry != 0:
                new_carry = (sum & carry) << 1
                sum = sum ^ carry
                carry = new_carry
        return sum
                
                
