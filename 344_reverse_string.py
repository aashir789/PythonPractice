'''
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

https://leetcode.com/problems/reverse-string/description/
'''

class Solution(object):
        def reverseString(self, s):
                    """
        :type s: str
        :rtype: str
        """
        new_string = ["0"] * len(s)
        for i in range(len(s)):
            p1, p2 = i, len(s) - 1 - i
            new_string[p1] = s[p2]
        return "".join(new_string)
