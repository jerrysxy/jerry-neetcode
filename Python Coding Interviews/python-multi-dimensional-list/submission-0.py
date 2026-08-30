from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    new_list = []
    #returns list of maximum element in each sub list
    #list only shld have max element in order.
    #nested_arr , list_in_list, elements
    for list_two in nested_arr:
        max_element = list_two[0]

        for elements in list_two:
            if elements > max_element:
                max_element = elements
        new_list.append(max_element)
    return new_list
    



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
