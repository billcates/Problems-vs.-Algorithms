def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return (None,None)
    if len(ints)==1:
        return (ints[0],ints[0])
    if len(ints)==2:
        return (ints[0],ints[1]) if ints[0]<ints[1] else (ints[1],ints[0])
    min_element=0
    max_element=0
    for each in ints:
        if each<min_element:
            min_element=each
        if each>max_element:
            max_element=each
    return (min_element,max_element)

#udacity testcases
print("Udacity testcas")
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#test testcases
#Null values
print("Null values passed")
print(get_min_max([[]]))#returns(None,None)
print(get_min_max([None]))#returns(None,None)
#Singelton values
print("Singleton values passed")
print(get_min_max([5]))#returns(5,5)
print(get_min_max([3]))#returns(3,3)
print(get_min_max([5879857648976875864896749]))#returns(5879857648976875864896749,5879857648976875864896749)
print("Negative values")
#Negative values
print(get_min_max([-5,-4]))
print(get_min_max([45,-12]))
print(get_min_max([-99]))
print("Only two values passed")
#two values passed
print(get_min_max([22,11]))
print(get_min_max([2233,11]))
print(get_min_max([76,0]))
print("very large numbers")
#very large test Case
l = [i for i in range(0, 100000)]  # a list containing 0 - 99999
random.shuffle(l)

print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")
