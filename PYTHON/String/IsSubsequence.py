# LeetCode Problem: 392. Is Subsequence from Leetcode 75
# https://leetcode.com/problems/is-subsequence/description/
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0
        if len(s) == 0: return True

        while(j < len(t) and i < len(s)):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

# Example usage:    
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # Output: True