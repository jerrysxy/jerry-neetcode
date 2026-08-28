from typing import List # used to add type hint for List

tally = 0

def count_x(nums: List[int], x: int) -> int:
    tally = 0

    for i in nums:
        if i == x:
            tally += 1
    return tally



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
