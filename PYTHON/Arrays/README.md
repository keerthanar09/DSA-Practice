## LeetCode 75 Problems

### Product of Array Except Self (22-07-2025)

- The suggested method in the description of the problem is using prefix and suffix products to calculate the product of all elements except self, HOWEVER, this method did not have the best time complexity (47 ms). 
- To improve time complexity to 19 ms, we can find the product of all elements and divide the product with the element at index "i" so that it's not included in the product
- The case where one or more elements of the array is `0` is handled seperately.

### Increasing Triplet (12-09-2025)

- Their final values at the moment of return might not correspond to the actual triplet's i and j, but the algorithm guarantees that some earlier i, j exist that pair with the found k.
- My initial instinct was to do this: 
```
for i in range(0, n-1):
        if i < i+1 < i+2 and nums[i] < nums[i+1] < nums[i+2]:
            return True
        else:
            continue
return False
```

- This worked for the first three given test cases, but I quickly realized that `i < j < k` obviously didn't mean that i, j and k had to be concequtive numbers and the condition could be satisfied even if i, j and k are 2, 3 and 5 respectively 😝

### Move Zeros (13-09-2025)

- This solution uses the `two pointer method`, where one of the pointers, `i`, keeps track of the zeros in the array, and `j` traverses the array. The elements are swapped when `nums[i] = 0` and `nums[j] != 0`

### Container With Most Water (14-09-2025)

- At first I used the brute force approach, but it wasn't accepted since it exceeded the time limit, so I took the better approach that uses the two pointer method since instead of iterating through every possible combination of i and j, the two pointer method only moves the pointers based on the `if height[i]<height[j]` statement.

### Max Number of K-Sum Pairs (14-09-2025)

- To avoid exceeding runtime limits, one key thing to always keep in mind is that questions can be decieving. Just because the problem mentions "removing pairs with k sum pairs till no such pairs exist", doesnt mean you need to physically remove the elements in the list, especially if the list itself doesn't have to be returned. 

### Maximum Average Subarray I (15-09-2025)

- Returning `max_sum*1.0/k` instead of `max_sum/k` was done to force float division, since without that, in leetcode, answer for the first test case came out as 12.000000 when it should've been 12.75 instead. 