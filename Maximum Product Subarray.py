''' Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6. '''



b=a[::-1]
for i in range(1,len(a)):
    a[i]*=a[i-1] or 1
    b[i]*=b[i-1] or 1
print(max(a+b))
