## LeetCode 75 Problems

### Reversing vowels in a string (17-07-2025)

- Time complexity = Space Complexity = O(N) for this solution.

### Reversing words in a string (22-07-2025)

- Time complexity = Space Complexity = O(N). Time complexity is 100% better than the other solutions, however this same method is only 55% better than the others when written in Java.

### String Compression (12-09-2025)

- Return `write` and not `len(chars)` since lists in python dont shrink, and write provides the new size of the compressed string.

### Is Subsequence (13-09-2025)

- A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., `"ace" `is a subsequence of `"abcde"` while `"aec"` is not).
- Again, don't make the mistake of assuming that a subsequence means the sequence needs to be concequtive letters in the original string. 🤦

### Longest Palindrome Substring (14-09-25)

- The method I used here is the brute-force method using two pointers to iteratively check the whole string for a palindrome substring. 
- (Performance can be better using DP)


## Other Problems

### Vowels game in a string - Does Alice Win? (12-09-2025)

- This is one of those questions that has a long description but once you figure out the conditions in which Alice loses or wins, it becomes really simple. 
- The only challenge was optimizing the time and space complexity.
- I learnt that its faster for a `for` loop to traverse through a set (Time complexity: O(1)) vs traversing through a string directly (Time complexity: O(n))

### Find Most Frequent Vowel and Consonant's Sum (13-09-2025)

- One thing I learned while solving this problem and trying to optimize it to balance the runtime and memory usage is that: `max()` function instead of the use of if statements in this problem will incur an overhead by checking for `max(max_v, v)` at every iteration. Hence sometimes, built-in functions may not be the best option just because they reduce the number of lines in the code. 

