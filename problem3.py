def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list ==[] or input_list is None:
        return None
    if len(input_list)<=2:
        print(input_list)
        return input_list
    descending_list=mergesort(input_list)
    str1='';str2=''
    for i in range(0,len(descending_list)):
        if i%2==0:
            str1+=str(descending_list[i])
        else:
            str2+=str(descending_list[i])
    print([int(str1),int(str2)])
    return int(str1),int(str2)
def mergesort(input_list):
    if len(input_list)<=1:
        return input_list
    l=len(input_list)//2
    left=mergesort(input_list[:l])
    right=mergesort(input_list[l:])
    return merge(left,right)
def merge(list1,list2):
    merged=[]
    list1_id=0
    list2_id=0
    while list1_id<len(list1) and list2_id<len(list2):
        if(list1[list1_id]>list2[list2_id]):
            merged.append(list1[list1_id])
            list1_id+=1
        else:
            merged.append(list2[list2_id])
            list2_id+=1
    merged+=list1[list1_id:]
    merged+=list2[list2_id:]
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    if test_case[0]==[] or test_case[0]==None:
        return None
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#test_cases
print("Udacity test cases")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
#when empty lsit is passed
print("when null values are passed")
print(test_function([[],[None]]))#returns None
print(test_function([None,[None]]))#returns None
#when singleton
print("when singleton value passed")
test_function([[3],[3]])
#when only two values are passed
print("when only two values are passed")
test_function([[2,3],[3,2]])
# general test_cases
print("general cases")
test_function([[1, 2], [2, 1]])
test_function([[1, 2,3], [32, 1]])
test_function ([[9,9], [9, 9]])
test_function([[1,2,3,4], [42, 31]])
test_function([[2,2,2,2,2], [222, 22]]) 
#larger values are passes
print("when larger values are passed")
test_function([[2,3,1,4,2,3,1,3,3,4,8,6,9,9,1,0,0], [984332110, 96433210]])
