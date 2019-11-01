"""
This is my game classes which I will use for game_interface.
"""
from typing import Any, List


class ChopsticksState:
    """
    A game state of Chopsticks.

    is_p1_turn - whether it is Player A's turn
    left_num_a - the number of left hand of Player A
    right_num_a - the number of right hand of Player A
    left_num_a - the number of left hand of Player B
    right_num_a - the number of right hand of Player B
    """
    def __init__(self, is_p1_turn: bool, hands: List[int]) -> None:
        """
        Initialize the State of Chopsticks.

        Precondition: left_num_a,right_num_a,left_num_b and right_num_b
        should all be between 0 and 5.
        """
        self.is_p1_turn = is_p1_turn
        self.left_num_a = hands[0]
        self.right_num_a = hands[1]
        self.left_num_b = hands[2]
        self.right_num_b = hands[3]

    def __str__(self) -> str:
        """
        Return the string representing the current state of Chopsticks.
        """
        return '...' + str(self.left_num_a) + '-' + \
               str(self.right_num_a) + '...' + \
               str(self.left_num_b) + '-' + \
               str(self.right_num_b) + '...'

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff all attributes of self is equal to those
        of other one by one.
        """
        return type(self) == type(other) \
               and self.left_num_a == other.left_num_a \
               and self.right_num_a == other.right_num_a \
               and self.left_num_b == other.left_num_b \
               and self.right_num_b == other.right_num_b

    def get_possible_moves(self):
        """
        Return a list containing all the possible moves.
        """
        if self.is_p1_turn:
            result = ['ll', 'lr', 'rl', 'rr']
            if self.left_num_a == 0:
                result[0] = ''
                result[1] = ''
            if self.right_num_a == 0:
                result[2] = ''
                result[3] = ''
            if self.left_num_b == 0:
                result[0] = ''
                result[2] = ''
            if self.right_num_b == 0:
                result[1] = ''
                result[3] = ''
            while '' in result:
                result.remove('')
            return result
        else:
            result = ['ll', 'lr', 'rl', 'rr']
            if self.left_num_b == 0:
                result[0] = ''
                result[1] = ''
            if self.right_num_b == 0:
                result[2] = ''
                result[3] = ''
            if self.left_num_a == 0:
                result[0] = ''
                result[2] = ''
            if self.right_num_a == 0:
                result[1] = ''
                result[3] = ''
            while '' in result:
                result.remove('')
            return result

    def is_valid_move(self, move: str) -> bool:
        """
        Return True iff move is an available move.
        """
        return move in self.get_possible_moves()

    def get_current_player_name(self) -> str:
        """
        Return the name of the current player.
        """
        if self.is_p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: str) -> "ChopsticksState":
        """
        Return the result of current state after the move.
        """
        if self.is_p1_turn:
            if move == 'll':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        self.right_num_a,
                                        (self.left_num_b + self.left_num_a)
                                        % 5,
                                        self.right_num_b])
            elif move == 'lr':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        self.right_num_a,
                                        self.left_num_b,
                                        (self.right_num_b + self.left_num_a)
                                        % 5])
            elif move == 'rl':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        self.right_num_a,
                                        (self.left_num_b + self.right_num_a)
                                        % 5,
                                        self.right_num_b])
            elif move == 'rr':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        self.right_num_a,
                                        self.left_num_b,
                                        (self.right_num_b + self.right_num_a)
                                        % 5])
        else:
            if move == 'll':
                return ChopsticksState(not self.is_p1_turn,
                                       [(self.left_num_a + self.left_num_b)
                                        % 5,
                                        self.right_num_a,
                                        self.left_num_b,
                                        self.right_num_b])
            elif move == 'lr':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        (self.right_num_a + self.left_num_b)
                                        % 5,
                                        self.left_num_b,
                                        self.right_num_b])
            elif move == 'rl':
                return ChopsticksState(not self.is_p1_turn,
                                       [(self.left_num_a + self.right_num_b)
                                        % 5,
                                        self.right_num_a,
                                        self.left_num_b,
                                        self.right_num_b])
            elif move == 'rr':
                return ChopsticksState(not self.is_p1_turn,
                                       [self.left_num_a,
                                        (self.right_num_a + self.right_num_b)
                                        % 5,
                                        self.left_num_b,
                                        self.right_num_b])
        return ChopsticksState(True, [0, 0, 0, 0])


class SquareState:
    """
    A game state of Subtract Square.

    is_p1_turn - whether it is Player A's turn
    value - the currnt value
    """
    def __init__(self, is_p1_turn: bool, value: int) -> None:
        """
        Initialize the State of Subtract Square.
        """
        self.is_p1_turn = is_p1_turn
        self.value = value

    def __str__(self) -> str:
        """
        Return the string representing the current state of Subtract Square.
        """
        return 'Current Value: ' + str(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff all attributes of self is equal to those
        of other one by one.
        """
        return type(self) == type(self) and self.value == other.value

    def get_possible_moves(self):
        """
        Return a list containing all the possible moves.
        """
        i = 1
        result = []
        while i * i <= self.value:
            result.append(i * i)
            i += 1
        return result

    def is_valid_move(self, move: int) -> bool:
        """
        Return True iff move is an available move.
        """
        return move in self.get_possible_moves()

    def get_current_player_name(self) -> str:
        """
        Return the name of the current player.
        """
        if self.is_p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: int) -> "SquareState":
        """
        Return the result of current state after the move.
        """
        return SquareState(not self.is_p1_turn, self.value - move)


class Game:
    """
    A game for a two-player, sequential move, zero-sum,
    perfect-information game.

    is_p1_turn - whether it is Player 1's turn to move
    """
    is_p1_turn: bool

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize this Game, is_p1-turn is True if Player 1 is moving now.
        """
        self.is_p1_turn = is_p1_turn

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff other is a game and its is_p1_turn is the
        same as self's.
        """
        return type(self) == type(other) and self.is_p1_turn == other.is_p1_turn

    def __str__(self) -> str:
        """
        Return a string representing the current state of the game.
        """
        return 'Game'

    def get_instructions(self) -> str:
        """
        Return a string for information of the game.
        """
        return 'Welcome to ' + str(self) + '!\nHave fun!\n'

    def is_over(self, current_state) -> bool:
        """
        Return True if the game is over..
        """
        return current_state.get_possible_moves() == []


class Chopsticks(Game):
    """
    A Chopsticks game, which is a son clas of Game.

    is_p1_turn - whether it is Player 1's turn to move
    current_state - the class ChopsticksState
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Create Chopsticks self which is a game.
        """
        Game.__init__(self, is_p1_turn)
        self.current_state = ChopsticksState(is_p1_turn, [1, 1, 1, 1])

    def __str__(self) -> str:
        """
        Return a string representing the Chopsticks.
        """
        return "'Chopsticks'"

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff self is equal to other.
        """
        return type(self) == type(other) and self.is_p1_turn == \
               other.is_p1_turn and self.current_state == other.current_state

    def str_to_move(self, inputs: str) -> str:
        """
        Return a move type by corresponding input.
        """
        return inputs

    def is_winner(self, player: str) -> bool:
        """
        Return True if someone wins.
        """
        if self.current_state.get_possible_moves() == []:
            return self.current_state.get_current_player_name() != player
        return False


class SubtractSquare(Game):
    """
    The Subtract Square game, which is a son class of Game.

    num - the current value
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the SubtractSquare. num is the start value.
        """
        Game.__init__(self, is_p1_turn)
        self.num = '-1'
        while (not self.num.isnumeric()) or int(self.num) < 0:
            self.num = input('Enter a non-negtive whole number: ')
        self.current_state = SquareState(is_p1_turn, int(self.num))

    def __str__(self) -> str:
        """
        Return a string representing the SubtractSquare.:
        """
        return "'Subtract Square'"

    def __eq__(self, other) -> bool:
        """
        Return True iff self is equal to other.
        """
        return type(self) == type(other) and self.num == other.num and \
               self.current_state == other.current_state

    def str_to_move(self, inputs: str) -> int:
        """
        Return a move type by corresponding input.
        """
        return int(inputs)

    def is_winner(self, player: str) -> bool:
        """
        Return True if someone wins.
        """
        if self.current_state.get_possible_moves() == []:
            return self.current_state.get_current_player_name() != player
        return False


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
