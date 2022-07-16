#---------------------------------------------------#
#---------------------CONSTANSTS--------------------#
#---------------------------------------------------#
HORIZONTAL_INDEX = 0
VERTICAL_INDEX = 1

LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3

#---------------------------------------------------#
#-------------------AUX FUNCTIONS-------------------#
#---------------------------------------------------#
def move_snake(snake : list, direction : int):
    """Creates a new snake in the given direction.

    Parameters
    ----------
    snake : list
        A list of cells (list of two ints) indicating the cells where the snake is. First cell is head and last tail.
    direction : int
        The direction to move the snake -> 0, 1, 2, 3 = LEFT, RIGHT, DOWN, UP
    
    
    Returns
    -------
    list
        A list of cells with the new snake
    """
    
    snake_copy = snake.copy()
    # Get the snake's head
    snakes_head = snake_copy[0]
    # Remove the tail of the snake
    snake_copy.pop()
    
    # Get the new head with the movement
    new_head = snakes_head.copy()
    if direction == LEFT:
        new_head[HORIZONTAL_INDEX] = new_head[HORIZONTAL_INDEX] - 1
    elif direction == RIGHT:
        new_head[HORIZONTAL_INDEX] = new_head[HORIZONTAL_INDEX] + 1
    elif direction == DOWN:
        new_head[VERTICAL_INDEX] = new_head[VERTICAL_INDEX] + 1
    elif direction == UP:
        new_head[VERTICAL_INDEX] = new_head[VERTICAL_INDEX] - 1
        
    # Insert the new head in snake's body
    snake_copy.insert(0, new_head)
    
    return snake_copy

def valid_snake(board : list, snake : list):
    """Check if the snake given is valid in the given board

    Parameters
    ----------
    board : list
        A list of length 2 with the dimensions of the board.
    snake : list
        A list of cells (list of two ints) indicating the cells where the snake is. First cell is head and last tail.
    
    Returns
    -------
    bool
        True if is valid, False if not
    """
    snakes_head = snake[0]
    snakes_body = snake[1:]
    
    # Self-intersection
    if snakes_head in snakes_body:
        return False
    
    # Inside of board borders
    if 0 <= snakes_head[HORIZONTAL_INDEX] < board[HORIZONTAL_INDEX] and 0 <= snakes_head[VERTICAL_INDEX] < board[VERTICAL_INDEX]:
        return True
    
    # Outsise of board borders
    return False

#---------------------------------------------------#
#---------------PRINCIPAL FUNCTIONS-----------------#
#---------------------------------------------------#
def number_of_available_different_paths(board : list, snake : list, depth : int, direction : int = None):
    """Get all the possibles paths for the snake in the board

    Parameters
    ----------
    board : list
        A list of length 2 with the dimensions of the board.
    snake : list
        A list of cells (list of two ints) indicating the cells where the snake is. First cell is head and last tail.
    depth : int
        The paths depth
    direction : int
        The direction to move the snake. None indicates that no movement has occur yet. -> 0, 1, 2, 3 = LEFT, RIGHT, DOWN, UP
    
    Returns
    -------
    int
        Number of possible paths, with the given depth, the snake can go. 
    """
    # Create the snake moved
    if direction is not None:
        snake = move_snake(snake, direction)
    
        # If the snake did an invalid movement, then return empty array
        if not valid_snake(board, snake):
            return 0

    # Stop condition, snake has move to the full depth. We have found a path!
    if depth == 0:
        return 1
    
    # Get the paths for every direction
    paths_left = number_of_available_different_paths(board, snake, depth-1, direction=LEFT) if (direction is None or direction != RIGHT) and snake[0][HORIZONTAL_INDEX] > 0 else 0
    paths_right = number_of_available_different_paths(board, snake, depth-1, direction=RIGHT) if (direction is None or direction != LEFT) and snake[0][HORIZONTAL_INDEX] < (board[HORIZONTAL_INDEX]-1) else 0
    paths_down = number_of_available_different_paths(board, snake, depth-1, direction=DOWN) if (direction is None or direction != UP) and snake[0][VERTICAL_INDEX] < (board[VERTICAL_INDEX]-1) else 0
    paths_up = number_of_available_different_paths(board, snake, depth-1, direction=UP) if (direction is None or direction != DOWN) and snake[0][VERTICAL_INDEX] > 0  else 0

    # Combine all partial solutions
    paths = paths_left + paths_right + paths_down + paths_up
    
    return paths