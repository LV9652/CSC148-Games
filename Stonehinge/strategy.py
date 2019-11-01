"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List
import copy
from trees_api_mond import Tree
from stack_api import Stack


def get_max1(game: Any, t: List[int]):
    """
    Return the score for the current state of game when it's player 1's turn.
    """
    if game.is_over(game.current_state):
        if game.is_winner('p1'):
            return 1
        elif game.is_winner('p2'):
            return -1
        return 0
    else:
        for move in game.current_state.get_possible_moves():
            game1 = copy.deepcopy(game)
            game1.current_state = game1.current_state.make_move(move)
            t.append(get_max1(game1, []))
        if not game.current_state.p1_turn and -1 in t:
            return -1
        return max(t)


def get_max2(game: Any, t: List[int]):
    """
    Return the score for the current state of game when it's player 2's turn..
    """
    if game.is_over(game.current_state):
        if game.is_winner('p1'):
            return -1
        elif game.is_winner('p2'):
            return 1
        return 0
    else:
        for move in game.current_state.get_possible_moves():
            game1 = copy.deepcopy(game)
            game1.current_state = game1.current_state.make_move(move)
            t.append(get_max2(game1, []))
        if game.current_state.p1_turn and -1 in t:
            return -1
        return max(t)


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.
def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return a move for game by recursive minimax strategy.
    """
    list1 = []
    if game.current_state.p1_turn:
        for move in game.current_state.get_possible_moves():
            game1 = copy.deepcopy(game)
            game1.current_state = game1.current_state.make_move(move)
            list1.append(get_max1(game1, []))
    else:
        for move in game.current_state.get_possible_moves():
            game1 = copy.deepcopy(game)
            game1.current_state = game1.current_state.make_move(move)
            list1.append(get_max2(game1, []))
    if 1 in list1:
        return game.current_state.get_possible_moves()[list1.index(1)]
    return game.current_state.get_possible_moves()[0]


# TODO: Implement an iterative version of the minimax strategy.
def iterative_minimax_strategy(game: Any) -> Any:
    """
    Return a move for game by iterative minimax strategy.
    """
    s = Stack()
    id1 = 0
    d = {0: Tree([id1, game, None])}
    s.add(0)
    while not s.is_empty():
        id2 = s.remove()
        items = [id2]
        if d[id2].children == []:
            for move in d[id2].value[1].current_state.get_possible_moves():
                game1 = copy.deepcopy(d[id2].value[1])
                game1.current_state = game1.current_state.make_move(move)
                id1 += 1
                d[id1] = Tree([id1, game1, None])
                d[id2].children.append(id1)
                items.append(id1)
        else:
            items.extend(d[id2].children)
        for num in items:
            if d[num].value[1].is_over(d[num].value[1].current_state):
                d[num].value[2] = -1
            elif d[num].children != [] and all(d[x].value[2] is not None
                                               for x in d[num].children):
                d[num].value[2] = max([(-1) * d[y].value[2]
                                       for y in d[num].children])
            else:
                s.add(num)
    i = 0
    for z in d[0].children:
        if d[z].value[2] == -1:
            i = d[0].children.index(z)
    return game.current_state.get_possible_moves()[i]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
