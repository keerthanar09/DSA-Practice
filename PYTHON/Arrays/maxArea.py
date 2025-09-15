# LeetCode 75 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_area = 0

        while i < j:
            max_area = max(min(height[i], height[j]) * (j-i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))