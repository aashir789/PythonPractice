'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

https://leetcode.com/problems/decode-ways/description/
'''
class Solution(object):
        def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s[0]) == 0 : return 0
        
        s = str(int(s))
        
        mat = [-1] * (len(s))
        mat[0] = 1
        for i in range(len(s)):
                if mat[i] != -1: continue
                last = int(s[i])
                second_last = int(s[i-1])
                third_last = int(s[i-2]) if i > 1 else None
                previous_decode = mat[i-1]
                pre_previous_decode = mat[i-2] if i > 1 else None
                
                if last == 0:
                        if second_last != 1 and second_last != 2:
                                return 0
                        elif i > 1 and (third_last == 1 or third_last == 2 ):
                                mat[i] = pre_previous_decode
                        else:
                                mat[i] = previous_decode
                elif (second_last*10 + last) < 10 or (second_last*10 + last) > 26:
                        mat[i] = previous_decode
                else:
                        mat[i] = pre_previous_decode + previous_decode if i > 1 else 2
        return mat[-1]
    
