## LeetCode 75 Problems

### Reversing vowels in a string (17-07-2025)

- Time complexity = Space Complexity = O(N) for this solution.

### Reversing words in a string (22-07-2025)

- Time complexity = Space Complexity = O(N). Time complexity is 100% better than the other solutions, however this same method is only 55% better than the others when written in Java.

### Product of Array Except Self (22-07-2025)

- The suggested method in the description of the problem is using prefix and suffix products to calculate the product of all elements except self, HOWEVER, this method did not have the best time complexity (47 ms). 
- To improve time complexity to 19 ms, we can find the product of all elements and divide the product with the element at index "i" so that it's not included in the product
- The case where one or more elements of the array is `0` is handled seperately.