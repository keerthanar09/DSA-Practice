#Leetcode-75: Program to reverse the vowels in a string, keeping the remaining string in the same order.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        start = 0
        end = len(s)-1
        vowels = "aeiouAEIOU"
        while (start < end):
            while (start < end and (l[start] not in vowels)):
                start = start + 1
            while (start < end and (l[end] not in vowels)):
                end = end - 1
            
            l[start], l[end] = l[end], l[start]
            start = start + 1
            end = end - 1
        
        return "".join(l)


s = Solution()
reverse = s.reverseVowels("Ice CreAm")
print(reverse)

