def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if number is None or number == [] or type(number)!=int:
        return None
    if input_list is None or len(input_list)==0:
        return None
    if len(input_list)==1 and input_list[0]!=number:
        return -1
    if len(input_list)>1:
        changed=find_pivot(input_list)
        #perform binary search on each list divided into at the pivot
        temp = binary_search(input_list[0: changed], number)
        if temp != -1:
            return temp
        temp = binary_search(input_list[changed: len(input_list)], number)
        if temp != -1:
            return temp + changed
        #number not found
        return -1
def binary_search(arr,number):
    start=0
    end=len(arr)-1
    last=end
    while start <=end and start<=last and end<=last:
        mid=(start+end)//2
        if arr[mid]==number:
            return mid
        if arr[mid]<number:
            start=mid+1
        elif arr[mid]>number:
            end=mid-1
    return -1
def find_pivot(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[start]<=arr[end]:
            return start
        elif arr[start]<=arr[mid]:
            start=mid+1
        else:
            end=mid
    return start
def linear_search(input_list, number):
    if number is None or number == [] or input_list ==[] or type(number)!=int:
        return None
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
#given test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#edge cases
test_function([[6, 7, 8, 1, 2, 3, 4],None])#returns None and prints Pass
print("empty number is traversed")
test_function([[6, 7, 8, 1, 2, 3, 4],[]])#return None and prints pass
print("empty input list")
test_function([[],34])#returns None when list is also empty
print("when a string is passed as a number to check")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4],"adhs"])#return None
print("very large comparison")
test_function([[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,1,2,3,4],10])
print("Singleton value")
test_function([[20],15])#returns -1 as value is not present and prints pass
