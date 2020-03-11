
number_grid = [
    #can make lists in a list
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#putting the index of the row and the column to call a specific value
print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)