"""
This is the stretegies of Games.
"""
from typing import Any
import random


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


# TODO: Implement a random strategy.
def random_strategy(game: Any) -> int:
    """
    Return a random move for game.
    """
    return game.str_to_move(game.current_state.get_possible_moves()
                            [random.randint(0, len(game.current_state.
                                                   get_possible_moves()) - 1)])


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
