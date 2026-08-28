from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    new_list = []
    for age in age_dict.values():
        new_list.append(age)
    return new_list

    #take dict of names and age
    #return list with only age
    

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
