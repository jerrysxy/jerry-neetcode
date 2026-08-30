from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    pass
    #r is index of row
    #c is index of column
    #true if cell [x,y,z] in grid: false otherwise
    rows = len(grid)
    column = len(grid[0])

    if rows >= r >= 0 and column >= c >= 0:
        return True
    else:
        return False

    

    # grid = [x,x,x],[x,x,x],[x,x,x]


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
