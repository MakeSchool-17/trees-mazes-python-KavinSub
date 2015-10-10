import maze
import stack
import random

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    backtrace = stack.Stack() # Create a stack for backtracking
    current_cell = random.randint(0, len(m.maze_array) - 1)  # Choose a cell index at random
    visited_cells = 1 # Set visited cells to 1
    while visited_cells < m.total_cells:
        unvisited = m.cell_neighbors(current_cell) # Get unvisited neighbors
        if len(unvisited) >= 1: # If at least one unvisited neighbor
            new_cell, compass_index = unvisited[random.randint(0, len(unvisited) - 1)] # Choose random neighbor to be new cell
            m.connect_cells(current_cell, new_cell, compass_index) # Knock down wall between cells
            backtrace.push(current_cell) # Push current cell to stack
            current_cell = new_cell # Set current cell to new cell
            visited_cells += 1 # Add 1 to visited cells
        else:
            current_cell = backtrace.pop() # Pop current cell from the stack
        m.refresh_maze_view() # Call refresh_maze_view
    m.state = 'solve'




def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
