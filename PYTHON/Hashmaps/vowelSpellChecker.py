# Leetcode problem 966. Vowel Spellchecker
# https://leetcode.com/problems/vowel-spellchecker/description/
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def remove_vowels(word):
            return "".join('*' if c in 'aeiouAEIOU' else c for c in word)
        ans = []
        words = set(wordlist)
        case_map = {}
        vowel_map = {}

        for w in wordlist:
            wl = w.lower()
            case_map.setdefault(wl, w)
            vowel_map.setdefault(remove_vowels(wl), w)
        
        def solve(query):
            if query in words:
                return query

            queryL = query.lower()
            if queryL in case_map:
                return case_map[queryL]

            queryLV = remove_vowels(queryL)
            if queryLV in vowel_map:
                return vowel_map[queryLV]
            return ""

        return map(solve, queries)

# Example usage:   
sol = Solution()
print(list(sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])))
# Output: ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']