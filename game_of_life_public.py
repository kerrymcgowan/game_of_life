"""Conway's Game of Life

.. module:: Project01
    :platform: Unix, Windows
    :synopsis: This script is a program that simulates Conway's Game of Life. It creates
        a 30 x 80 grid where a '-' means "off" and an 'X' means "on".
        The number of time points the script will run for and the initial "on" cells are input
        as arguments by the user.
        The program will print the grid for each time point following the rules of the game.
        The rules are as follows:
           * Any “on” cell with fewer than two live neighbors is turned “off”.
           * Any “on” cell with two or three “on” neighbors remains “on”.
           * Any “on” cell with more than three “on” neighbors is turned “off”.
           * Any “off” cell with exactly three live neighbors is turned “on”.
           * A neighbor is any adjacent cell, including those to the East, West,
             North, South, Northeast, Northwest, Southeast and Southwest of the cell.

.. moduleauthor:: Kerry McGowan

"""

# Import the command line arguments for the script using argv, part of the sys module.
from sys import argv

def create_grid(nrows, ncols):
    """Create a grid.

    This function initializes an empty grid, then populates it with all zeros.

    :param nrows:  The number of rows in the grid.
    :type nrows:  An integer.

    :param ncols:  The number of columns in the grid.
    :type ncols:  An integer.

    """
    # Create an empty list named grid.
    grid = []
    # Populate the grid with zeros.
    for i in range(nrows):
        grid.append([0] * ncols)
    # Return the grid.
    return(grid)

def print_grid(grid, nrows, ncols):
    """Print the grid.

    This function prints the grid to the screen.

    :param grid: A square of '-' for "off" and 'X' for "on".
    :type grid: A list.

    :param nrows: The number of rows in the grid.
    :type nrows: An integer.

    :param ncols: The number of columns in the grid.
    :type ncols: An integer.

    """
    for i in range(nrows):
        #print(i+1, end="")
        for j in range(ncols):
            # Print '-' for "off" cells.
            if grid[i][j] == 0:
                print('-', end='')
            # Print 'X' for "on" cells.
            else:
                print('X', end='')
        # The end of each row must end in a new line character.
        print("\n", end='')

def apply_rules(grid, nrows, ncols):
    """ Implement the rules of the game and adjust the grid accordingly.

    This function first creates a new grid (new_grid) populated with all zeros. For each cell in the
    grid, it then looks to see if each neighboring cell in the grid is a 1 or 0 and sets that value
    equal to a variable named by its cardinal or ordinal direction. The total number of neighbors is
    then summed. The new grid (new_grid) is then populated with the 0s and 1s of the old grid (grid)
    and the rules of the game are applied to turn cells on, off, or leave them as their orginal state.

    :param grid: A square of '-' for "off" and 'X' for "on".
    :type grid: A list.

    :param nrows: The number of rows in the grid.
    :type nrows: An integer.

    :param ncols: The number of columns in the grid.
    :type ncols: An integer.

    """
    # Create a new list called grid populated with all 0s.
    new_grid = create_grid(nrows, ncols)
    # Count the neighbors that are on.
    for i in range(nrows):
        for j in range(ncols):
            # Anything with a + will not wrap at the edge of the grid, so if/else statements are needed
            # Northwest neighbors.
            nw = grid[i-1][j-1]
            # North neighbors.
            n  = grid[i-1][j]
            # Northeast neighbors.
            if j+1 >= ncols:
                ne = grid[i-1][0]
            else:
                ne = grid[i-1][j+1]
            # West neighbors.
            w  = grid[i][j-1]
            # Southwest neighbors.
            if i+1 >= nrows:
                sw = grid[0][j-1]
            else:
                sw = grid[i+1][j-1]
            # South neighbors.
            if i+1 >= nrows:
                s  = grid[0][j]
            else:
                s  = grid[i+1][j]
            # Southeast neighbors.
            if i+1 >= nrows or j+1 >= ncols:
                se = grid[0][0]
            else:
                se = grid[i+1][j+1]
            # East neighbors.
            if j+1 >= ncols:
                e  = grid[i][0]
            else:
                e  = grid[i][j+1]
            # Sum neighbors from all directions.
            neighbors = nw + n + ne + w + sw + s + se + e
            # To change the new_grid, first must copy over values from grid into new_grid.
            new_grid[i][j]=grid[i][j]
            # Apply the rules.
            if new_grid[i][j] == 1:
                # Rule: Any “on” cell with fewer than two live neighbors is turned “off”, i.e., cell changes from 1 to 0.
                if neighbors < 2:
                    new_grid[i][j] = 0
                # Any “on” cell with two or three “on” neighbors remains “on”, i.e., cell stays 1.
                elif neighbors == 2 or neighbors == 3:
                    pass
                # Rule: Any “on” cell with more than three “on” neighbors is turned “off”, i.e., cell changes from 1 to 0.
                elif neighbors > 3:
                    new_grid[i][j] = 0
            else:
                # Rule: Any “off” cell with exactly three live neighbors is turned “on”, i.e., cell changes from 0 to 1.
                if neighbors == 3:
                    new_grid[i][j] = 1
    # Return the new grid that has now been changed by the rules.
    return(new_grid)

def main():
    """This is the main executable function in this script.

    This function sets the number of time points the program runs (n_ticks) as well as the number
    of start cells (start_cells) that will be populated by an 'X' instead of a '-'.

    The grid is then initialized with 30 rows and 80 columns.

    The start cells are split into their rows and columns and 0 is replaced with a 1 in
    those positions in the grid.

    The grid is then printed and rules of the game applied. This repeats for the number of
    time points specified by the user.

    """
    # Set the command-line arguments (n_ticks, start_cells [which can be a variable number of cells]) equal to variables.
    # n_ticks is the number of time points the script will run for.
    n_ticks = argv[1]
    # start_cells is/are the cell(s) that are populated by an 'X' and are thus considered "on".
    # Note that incoming cell indices are 1-based not 0-based.
    start_cells = argv[2:]

    #print(n_ticks)
    #print(start_cells)

    # Initialize the grid.
    # Set number of rows in the grid equal to nrows.
    nrows = 30
    # Set number of columns in the grid equal to ncols.
    ncols = 80
    # Create a list of zeros called grid using the number of rows and columns specified above.
    grid = create_grid(nrows, ncols)

    # Set the starting cells specified by the user that will be populated by an 'X'.
    for start_cell in start_cells:
        #print(start_cell)
        # Split the cell indices by the colon that separates row:column. i is the row and j is the column.
        i, j = start_cell.split(':')
        #print("{} {}".format(i,j))
        # Subtract 1 from the row value because cell indices are 1-based not 0-based (and the grid is 0-based).
        i = int(i) - 1
        # Subtract 1 from the column value because cell indices are 1-based not 0-based (and the grid is 0-based).
        j = int(j) - 1
        # Set the start cell equal to 1.
        grid[i][j] = 1

    # Iterate through the number of time points (n_ticks) set by the user.
    # Note: 1 is added to the number of ticks set by the user because the program interprets initializing the grid as step 1,
    # when it is actually step 0.
    for i in range(int(n_ticks)+1):
        # Call the function print_grid to print the grid to the screen.
        print_grid(grid, nrows, ncols)
        # Call the function apply_rules to apply the rules of the game, and replace the variable grid with the changed list of 1s and 0s.
        grid = apply_rules(grid, nrows, ncols)

# Call the module main on the command line.
if __name__ == "__main__":
    main()
