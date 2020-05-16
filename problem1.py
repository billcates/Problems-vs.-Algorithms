def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return None
    if number<0:
        return -1
    if number is 0:
        return 0
    else:
        left,right = 1, number
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= number and (mid + 1) **2 > number:
                return mid
            elif mid ** 2 > number:
                right = mid - 1
            elif mid ** 2 < number:
                left = mid + 1
        return left
#test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (11 == sqrt(121)) else "Fail")
#edge case 1
print("pass "if (None==sqrt(None))else"Fail")
#edge case 2
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#edge case 3
print("Pass " if (-1==sqrt(-45))else "Fail")
