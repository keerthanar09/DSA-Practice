# Leetcode problem 3541: Find most frequent vowel and consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        max_v = max_c = 0
        for i in s:
                freq[i] = freq.get(i, 0)+1
                
        for k, v in freq.items():
            if k in "aeiouAEIOU":
                if v > max_v:
                    max_v = v
            elif v > max_c:
                max_c = v
        
        return max_c + max_v
# Example usage:
sol = Solution()
print(sol.maxFreqSum("abcde"))  # Output: 3