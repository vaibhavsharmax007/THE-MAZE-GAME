"""
Maze Escape Game  (PS 63)
-------------------------
- The maze is a 2D list (a list of lists).
- Move with W (up), A (left), S (down), D (right).
- Walls (#) block movement. You cannot leave the maze.
- Reach E to win.
- Menu option 2 finds the shortest path using BFS.
"""


# 1. THE MAZE  (# = wall, . = path, P = start, E = exit)

maze = [
    ['P', '.', '.', '#', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', '#', '#'],
    ['#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', 'E'],
]

ROWS = len(maze)       # number of rows    -> 5
COLS = len(maze[0])    # number of columns -> 5

START = (0, 0)         # player starts at row 0, col 0
EXIT = (4, 4)          # exit is at row 4, col 4



# 2. SHOW THE MAZE ON SCREEN

def print_maze(player_row, player_col, path=None):
    """Prints the maze. The player is shown as P.
    If a path (list of positions) is given, it is shown with * marks."""
    if path is None:
        path = []

    print()
    for r in range(ROWS):
        line = ""
        for c in range(COLS):
            if (r, c) == (player_row, player_col):
                line += "P "
            elif (r, c) in path and maze[r][c] == '.':
                line += "* "
            elif maze[r][c] == 'P':
                line += ". "      # the old start square is just a path
            else:
                line += maze[r][c] + " "
        print(line)
    print()



# 3. PLAY THE GAME

def play_game():
    row, col = START       # current position of the player
    moves = 0              # only VALID moves are counted

    print("\nUse W (up), A (left), S (down), D (right). Type Q to quit.")
    print_maze(row, col)

    while True:
        key = input("Your move: ").strip().upper()

        # Quit option
        if key == 'Q':
            print("You quit the game.")
            return

        # Work out where the player WANTS to go
        new_row, new_col = row, col
        if key == 'W':
            new_row = row - 1
        elif key == 'S':
            new_row = row + 1
        elif key == 'A':
            new_col = col - 1
        elif key == 'D':
            new_col = col + 1
        else:
            print("Invalid key '" + key + "'. Use W, A, S or D only.")
            continue          # go back and ask again

        # Check 1: is the new position outside the maze?
        if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
            print("Cannot move outside the maze. Player stays at ("
                  + str(row) + ", " + str(col) + ").")
            print("Moves:", moves)
            continue

        # Check 2: is there a wall?
        if maze[new_row][new_col] == '#':
            print("Wall ahead. Move blocked. Player stays at ("
                  + str(row) + ", " + str(col) + ").")
            print("Moves counted:", moves)
            continue

        # The move is valid, so update the player's position
        row, col = new_row, new_col
        moves += 1
        print("Player moved to (row " + str(row) + ", col " + str(col)
              + ") | Moves: " + str(moves))
        print_maze(row, col)

        # Check 3: did the player reach the exit?
        if maze[row][col] == 'E':
            print("You escaped the maze! Total moves:", moves)
            return



# 4. FIND THE SHORTEST PATH (BFS)

def find_shortest_path():
    """BFS = Breadth First Search.
    It explores the maze step by step, like ripples in water, so the
    first time it reaches the exit, that route is the shortest one."""

    # Each item in the queue is: (row, col, path_taken_so_far)
    queue = [(START[0], START[1], [START])]
    visited = [START]      # squares we have already checked

    while len(queue) > 0:
        row, col, path = queue.pop(0)   # take the first item in the queue

        # Reached the exit? Then this path is the shortest.
        if (row, col) == EXIT:
            return path

        # Try all 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col

            inside = 0 <= new_row < ROWS and 0 <= new_col < COLS
            if inside and maze[new_row][new_col] != '#' \
                    and (new_row, new_col) not in visited:
                visited.append((new_row, new_col))
                queue.append((new_row, new_col, path + [(new_row, new_col)]))

    return None   # no path exists


def show_shortest_path():
    path = find_shortest_path()
    if path is None:
        print("No path found!")
        return

    steps = len(path) - 1   # number of moves = squares minus 1
    print("\nShortest path (marked with *):")
    print_maze(EXIT[0], EXIT[1], path)
    print("Path:", path)
    print("Shortest path length:", steps, "steps")


# 5. MAIN MENU

def main():
    print("=== MAZE ESCAPE GAME ===")
    while True:
        print("\n1. Play the game")
        print("2. Show shortest path")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            play_game()
        elif choice == '2':
            show_shortest_path()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2 or 3.")


# This line runs main() when you start the file
main()