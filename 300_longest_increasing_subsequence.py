'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

https://leetcode.com/problems/longest-increasing-subsequence/description/
'''
class Solution(object):
        def lengthOfLIS(self, nums):
                """
                :type nums: List[int]
                :rtype: int
                """
                in not nums: return 0
                dp = [0] * len(nums)
                tail = [0] * len(nums)
                dp[0] = 1
                for i in range(len(nums)):
                        dp_to_consider = []
                        for j in range(i):
                                if nums[j] < nums[i]: dp_to_consider.append(dp[j])
                        if not dp_to_consider: dp[i] = 1
                        longest_sequence = max(dp_to_consider)
                        dp[i] = longest_sequence + 1
                return max(dp)
