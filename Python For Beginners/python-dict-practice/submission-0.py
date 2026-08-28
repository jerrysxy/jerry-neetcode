from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    #make a dictionary first
    counts = {}
# for each letter in word
    for letter in word:

        if letter not in counts:
            counts[letter] = 1
        elif letter in counts:
            counts[letter] += 1

    return counts



    # take string, word, count how many of each letter
    # key: letter value: how many




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
