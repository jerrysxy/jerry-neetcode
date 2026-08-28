from typing import List

def contains_duplicate(words: List[str]) -> bool:
    length_list = len(words)
    # list length not equal to set means theres duplicates
    #return true
    words_set = set(words)
    length_set = len(words_set)

    if length_list != length_set:
        return True
    else:
        return False
    # list length same as set means no duplicates
    # return false

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
