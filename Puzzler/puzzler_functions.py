"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view
 

def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if puzzle is the same as view or
    current_selection is QUIT.
    
    Precondition: current_selection must be one of 'C','V','S' and 'Q'.
    
    >>>game_over('banana', 'ba^a^a',SOLVE)
    False
    >>>game_over('apple', 'apple', VOWEL)
    True
    >>>game_over('pear', 'p^^r', QUIT)
    True
    """
    return puzzle == view or current_selection == QUIT


def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if letter is in the puzzle but not in view.
    
    Precondition: letter must contain only one letter.
    
    >>>bonus_letter('banana', '^^n^n^', 'b')
    True
    >>>bonus_letter('banana', '^^n^n^', 'n')
    False
    >>>bonus_letter('apple', 'a^^l^', 'm')
    False
    """
    return letter in puzzle and not letter in view


def update_letter_view(puzzle: str, view: str, index: int, guessed_letter: str) -> str:
    """Return the character at the index of puzzle if the character at that 
    index of the puzzle is same as guessed_letter, then return that character. 
    Otherwise, return the character at that index of view.
    
    Precondition: index <= len(puzzle).
                  guessed_letter must contain only one letter and haven't been 
                  guessed before.
    
    >>>update_letter_view('banana', 'b^^^^^', 3, 'n')
    '^'
    >>>update_letter_view('banana', 'b^^^^^', 3, 'a')
    'a'
    """
    if guessed_letter == puzzle[index]:
        return puzzle[index]
    else:
        return view[index]
  
    
def calculate_score(current_score: int, occurrence: int, letter_type: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per occurrence to 
    current_score if letter_type is CONSONANT, or by deducting VOWEL_PRICE 
    from current_score if letter_type is VOWEL.
    
    Precondition: letter_type must be CONSONANT or VOWEL.
    
    >>>calculate_score(5, 2, CONSONANT)
    7
    >>>calculate_score(4, 4, VOWEL)
    3
    """
    if letter_type == CONSONANT:
        return current_score + occurrence * CONSONANT_POINTS
    elif letter_type == VOWEL:
        return current_score - VOWEL_PRICE
   
    
def next_player(current_player: str, occurrence: int) -> str:
    """Return the next player. Return current_player if and only if occurrence 
    is greater than zero. Otherwise, return the other player (one of PLAYER_ONE 
    or PLAYER_TWO).
    
    Precondition: current_player must be PLAYER_ONE or PLAYER_TWO.
    
    >>>next_player(PLAYER_ONE, 3)
    'PLAYER_One'
    >>>next_player(PLAYER_TWO, 0)
    'PLAYER_One'
    """
    if occurrence > 0:
        return current_player
    if occurrence == 0:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE
        