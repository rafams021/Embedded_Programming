import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    total = 0

    #
    # TODO - implement this in part 2
    #
        
    for value in range(len(grid)):      #len(grid) == to height
        new_row = []
        for value2 in range(len(grid[0])):      #len(grid[0]) == to width
            hit = (color == grid[value][value2])
            new_belief = beliefs[value][value2] * (hit * p_hit + (1 - hit) * p_miss)
            total = total + new_belief
            new_row.append(new_belief)
        new_beliefs.append(new_row)
        
    #Normalize
    for value in range(len(grid)):      #len(grid) == to height
        for value2 in range(len(grid[0])):      #len(grid[0]) == to width
            new_beliefs[value][value2] = new_beliefs[value][value2] / total
            
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)