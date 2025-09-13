# Leetcode 75: 3227 - https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12
class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
    #Alice only loses if there are no vowels in the string. Shes always guarenteed a win regardless if the vowel is even or not.
        vowels = set("aeiouAEIOU")
        for c in s:
            if c in vowels:
                return True
            
        return False
sol = Solution()
print(sol.doesAliceWin("hello"))