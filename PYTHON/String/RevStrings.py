#Leetcode 75 - Reverse the words in an input string (Medium).
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sm = s.strip().split()
        rev = []
        for i in reversed(sm):
            rev.append(i)

        return " ".join(rev)
    
sol = Solution()
print(sol.reverseWords("the sky is blue"))