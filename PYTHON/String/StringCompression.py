class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        write = 0
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1 
            else:
                chars[write] = chars[i-1]
                write += 1
                if count>1:
                    for d in str(count):
                        chars[write] = d
                        write += 1

                count = 1
        return write

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))