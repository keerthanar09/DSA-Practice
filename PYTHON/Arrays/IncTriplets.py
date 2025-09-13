class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        n = len(nums)
        for n in nums:
            if n <= first:
                first = n
            elif n <=second:
                second = n
            else:
                return True
        return False

sol = Solution()
print(sol.increasingTriplet([2,1,5,0,4,6]))