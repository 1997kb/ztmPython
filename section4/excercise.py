#given 2 arrays
#identify if the two arrays contains common items
#if it does return True, else False

array1 = ['a','b','c','x']
array2 = ['z','y','i','a']

#O(1) time complexity no loops involed and space complexity O(1)
# def solution(length_set,length_combined):
#     if length_combined != length_set:
#         return True
#     else:
#         return False

# combined_list = array1 + array2 #O(m + n) time complexity as it involves two lists and linear operation on both lists and O(n+m) space complexity
# list_array = set(combined_list)#O(m+n) time complexity and O(k) space complexity as k unique elements are stored
# print(solution(len(list_array),len(combined_list)))


#improved solution


def checkForCommon(array1,array2):
    list_set = set(array1)
    for i in array2:
        if i in list_set:
            return True
    return False


print(checkForCommon(array1,array2))
  




