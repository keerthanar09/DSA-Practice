#Leetcode Problem - Find the length of the longest substring with no repeated letters in the given string.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        maxlength = 0
        ch = set()

        for j in range(len(s)):
            while s[j] in ch:
                ch.remove(s[i])
                i+=1
            ch.add(s[j])
            maxlength = max(maxlength, j-i+1)
        return maxlength

sol = Solution()
print(sol.lengthOfLongestSubstring("abcbabdbabeabdbebc"))