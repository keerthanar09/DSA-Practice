# Leetcode problem 283: Move Zeroes, from LeetCode 75
# https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        n = len(nums)-1
        while j!=n:
            j += 1
            if nums[i] != 0:
                i += 1
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            

sol = Solution()
arr = [0,1,0,3,12]
sol.moveZeroes(arr)
print(arr) # Output: [1, 3, 12, 0, 0]