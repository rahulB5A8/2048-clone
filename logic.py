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






