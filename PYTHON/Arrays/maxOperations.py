# Leetcode 75. Problem 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = count = 0
        j = len(nums)-1

        while(i<j):
            if nums[i] + nums[j] == k:
                i+=1
                j-=1
                count += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return count


sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))
