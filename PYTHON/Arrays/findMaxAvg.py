# Leetcode 75. Problem 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)

        return max_sum*1.0/k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))