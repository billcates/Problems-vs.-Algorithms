Square root of a number:
  The sqrt of a number can be easly found bt just putting(number ** 0.5) which
  absolutely gives the sqrt,but it tales O(n/2).Therefore we use binary search
  to find the sqrt of a number.
  *Iteratively find the middle element of the numbers range form left to right and compare with the number when the value is less than number make mid+1 as leftt and if value is large then,mid-1=end
  *When iteration ends,return the left value,which will be our square root.
Time Complexity:
  Binary Search O(logn)
Space Complexity:
  O(1) 
