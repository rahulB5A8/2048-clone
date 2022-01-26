import random

def start_game():
    arr = []
    for row_index in range(4):
        arr.append([0]*4)    
    return arr

def add_new_2(arr):
    row = random.randint(0,3)
    col = random.randint(0,3)
    while(arr[row][col] != 0):
        row = random.randint(0,3)
        col = random.randint(0,3)
    
    arr[row][col] = 2
    return arr

def reverse(arr):
    new_arr = []
    for row_index in range(4):
        new_arr.append([])
        for col_index in range(4):
            new_arr[row_index].append(arr[row_index][4-col_index-1])
    
    return new_arr

def transpose(arr):
    new_arr = []
    for row_index in range(4):
        new_arr.append([])
        for col_index in range(4):
            new_arr[row_index].append(arr[col_index][row_index])
    
    return new_arr

def merge(arr):
    for row_index in range(4):
        for col_index in range(3):
            if arr[row_index][col_index] == arr[row_index][col_index+1] and arr[row_index][col_index]!=0:
                arr[row_index][col_index] = arr[row_index][col_index]*2
                arr[row_index][col_index+1] = 0    
    
    return arr

def compress(arr):
    new_arr = []
    for row_index in range(4):
        new_arr.append([0]*4)
        
        for row_index in range(4):
            pos = 0
            for col_index in range(4):
                if arr[row_index][col_index] != 0:
                    new_arr[row_index][pos] = arr[row_index][col_index]
                    pos+=1

    return new_arr

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid = compress(transposed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    
    return final_grid

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    
    return final_grid

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    
    return final_grid

def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    
    return new_grid

def get_current_state(arr):
    
    # Anywhere 2048 is present
    for row_index in range(4):
        for col_index in range(4):
            if (arr[row_index][col_index] == 2048):
                return 'WON!!!!'
    
    #Anywhere 0 is present
    for row_index in range(4):
        for col_index in range(4):
            if(arr[row_index][col_index] == 0):
                return '--------Still all to play for--------------'

    # Every Row and Column except last row and last column
    for row_index in range(3):
        for col_index in range(3):
            if(arr[row_index][col_index] == arr[row_index+1][col_index] or arr[row_index][col_index] == arr[row_index][col_index+1]):
                return '--------Still all to play for--------------'

    #Last Row
    for col_index in range(3):
        if arr[3][col_index] == arr[3][col_index+1]:
            return '--------Still all to play for--------------'

    #Last Column
    for row_index in range(3):
        if arr[row_index][3] == arr[row_index+1][3]:
            return '--------Still all to play for--------------'
    
    return 'LOST'

arr = start_game()
arr[1][3] = 2
arr[2][2] = 2
arr[3][0] = 4
arr[3][1] = 8
arr[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
    arr = move_up(arr)
    elif ele == 2:
    arr = move_down(arr)
    elif ele == 3:
    arr = move_left(arr)
    else:
    arr = move_right(arr)
    print(arr)


