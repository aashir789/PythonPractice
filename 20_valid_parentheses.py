'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

https://leetcode.com/problems/valid-parentheses/description/
'''

class Solution(object):
        def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        closing = {")", "}", "]"}
        opening = {"(", "{", "["}
        closing_dict = {")":"(","}":"{","]":"["}
        
        for char in s:
            if char in opening:
                l.append(char)
            elif char in closing:
                if closing_dict[char] != l[-1]:
                    return False
                else:
                    l.pop()
            else:
                return False

        if l:
            return False
        return True
