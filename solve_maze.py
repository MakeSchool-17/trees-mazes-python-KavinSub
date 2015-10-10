import maze
import generate_maze
import sys
import stack
import collections
import random

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    backtrace = stack.Stack() # Create Stack
    current_cell = 0
    visited_cells = 0

    while current_cell != len(m.maze_array) - 1: # While current cell is not goal
        unvisited = m.cell_neighbors(current_cell)
        if len(unvisited) >= 1:
            new_cell, compass_index = unvisited[random.randint(0, len(unvisited) - 1)]
            m.visit_cell(current_cell, new_cell, compass_index)
            backtrace.push(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = backtrace.pop()
        m.refresh_maze_view()
    m.state = 'idle'

# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    queue = collections.deque()
    current_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.append((current_cell, in_direction))

    while current_cell != len(m.maze_array) - 1 and len(queue) != 0:
        current_cell, in_direction = queue.popleft()
        m.bfs_visit_cell(current_cell, in_direction) # Not sure about this one...
        visited_cells += 1
        m.refresh_maze_view()

        unvisited = m.cell_neighbors(current_cell)
        for i in range(len(unvisited)):
            queue.append(unvisited[i])

    m.reconstruct_solution(current_cell)

    m.state = 'idle'

def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
