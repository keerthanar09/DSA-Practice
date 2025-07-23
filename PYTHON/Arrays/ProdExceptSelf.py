#Leetcode 75 - Product of array except self (Medium)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prod = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                prod *= i
            else: 
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        
        for i in nums:
            if i != 0:
                if zero_count == 1:
                    ans.append(0)
                else: 
                    ans.append(prod//i)
            else:
                ans.append(prod)
        return ans


sol = Solution()
print(sol.productExceptSelf([1,2,3,4,5]))