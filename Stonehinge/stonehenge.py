"""
An implementation of Stonehenge.
"""
from typing import Any, List
from game_state import GameState
from game import Game


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool,
                 comlist: List[List[str]], n: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.n = n
        self.list = comlist
        self.row_marker = []
        self.downleft_marker = []
        self.downright_marker = []
        i = 0
        while i < n + 1:
            self.row_marker.append('@')
            self.downleft_marker.append('@')
            self.downright_marker.append('@')
            i += 1

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff self is equal to other.
        """
        return type(self) == type(other) and \
               self.n == other.n and \
               self.list == other.list and \
               self.row_marker == other.row_marker and \
               self.downleft_marker == other.downright_marker and \
               self.downright_marker == other.downright_marker

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        result = '\\ \n' + ' ' * (4 + self.n * 2) + self.downleft_marker[0] \
                 + '   ' + self.downleft_marker[1] + '\n' \
                 + ' ' * (3 + self.n * 2) + '/' + '   ' + '/' + '\n'
        result1 = []
        result2 = []
        for i in range(self.n - 1):
            result1.append(self.row_marker[i] + ' - '
                           + ' - '.join(x for x in self.list[i])
                           + '   ' + self.downleft_marker[i + 2])
            result2.append('/ \\ ' * (i + 2) + '/')
        result1.append(self.row_marker[self.n - 1] + ' - '
                       + ' - '.join(x for x in self.list[self.n - 1]))
        result1.append(self.row_marker[self.n] + ' - '
                       + ' - '.join(x for x in self.list[self.n])
                       + '   ' + self.downright_marker[0])
        result2.append('\\ / ' * self.n + '\\')
        result2.append('\\   ' * self.n)
        for j in range(self.n - 1):
            result += ' ' * (self.n * 2 - 2 - j * 2) + result1[j] + '\n'
            result += ' ' * (self.n * 2 + 1 - j * 2) + result2[j] + '\n'
        result += result1[self.n - 1] + '\n' \
                  + ' ' * 5 + result2[self.n - 1] + '\n' \
                  + ' ' * 2 + result1[self.n] + '\n' \
                  + ' ' * 7 + result2[self.n] + '\n' \
                  + ' ' * 8
        for k in range(1, self.n + 1):
            result += self.downright_marker[-k] + '   '
        return result.rstrip()

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        whole = self.row_marker + self.downleft_marker + self.downright_marker
        if whole.count('1') >= (self.n * 3 + 3) / 2 \
                or whole.count('2') >= (self.n * 3 + 3) / 2:
            return []
        result = []
        for cells in self.list:
            for cell in cells:
                if cell in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N',
                            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                            'V', 'W', 'X', 'Y', 'Z']:
                    result.append(cell)
        return result

    def list_downleft(self) -> list:
        """
        Return the index of the down-left line which letter belongs to.
        """
        result = []
        i = 0
        k = 1
        while i < self.n + 1:
            result.append([cells[i]
                           for cells in self.list[:self.n]
                           if i <= len(cells) - 1])
            i += 1
        for cell in self.list[self.n]:
            result[k].append(cell)
            k += 1
        return result

    def list_downright(self) -> list:
        """
        Return the index of the down-right line which letter belongs to.
        """
        result = []
        i = 1
        k = 1
        while i < self.n + 2:
            result.append([cells[-i]
                           for cells in self.list[:self.n]
                           if i <= len(cells)])
            i += 1
        while k < self.n + 1:
            result[k].append(self.list[self.n][-k])
            k += 1
        return result

    def change_marker(self, i: int, j: int, k: int) -> None:
        """
        Change the state of row, down-left and
        down-right markers by indices i, j and k.
        """
        if self.row_marker[i] == '@':
            if self.list[i].count('1') >= len(self.list[i]) / 2:
                self.row_marker[i] = '1'
            elif self.list[i].count('2') >= len(self.list[i]) / 2:
                self.row_marker[i] = '2'
        if self.downleft_marker[j] == '@':
            if self.list_downleft()[j].count('1') \
                    >= len(self.list_downleft()[j]) / 2:
                self.downleft_marker[j] = '1'
            elif self.list_downleft()[j].count('2') \
                    >= len(self.list_downleft()[j]) / 2:
                self.downleft_marker[j] = '2'
        if self.downright_marker[k] == '@':
            if self.list_downright()[k].count('1') \
                    >= len(self.list_downright()[k]) / 2:
                self.downright_marker[k] = '1'
            elif self.list_downright()[k].count('2') \
                    >= len(self.list_downright()[k]) / 2:
                self.downright_marker[k] = '2'

    def make_move(self, move: str) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        result = StonehengeState(self.p1_turn,
                                 [a[:] for a in self.list], self.n)
        result.row_marker = self.row_marker[:]
        result.downleft_marker = self.downleft_marker[:]
        result.downright_marker = self.downright_marker[:]
        i = 0
        for line in result.list_downleft():
            if move in line:
                j = result.list_downleft().index(line)
        for line in result.list_downright():
            if move in line:
                k = result.list_downright().index(line)
        m = 0
        while i < result.n + 1:
            m = 0
            while m < len(result.list[i]):
                if result.list[i][m] == move:
                    result.list[i][m] = '1' if result.p1_turn else '2'
                    result.change_marker(i, j, k)
                m += 1
            i += 1
        result.p1_turn = not result.p1_turn
        return result

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: " + str(self.p1_turn) \
               + "\n" + 'Current State: ' + '\n' + str(self)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        result = []
        whole = self.row_marker + self.downleft_marker + self.downright_marker
        if whole.count('1') >= (self.n * 3 + 3) / 2:
            return 1 if self.p1_turn else -1
        elif whole.count('2') >= (self.n * 3 + 3) / 2:
            return -1 if self.p1_turn else 1
        for move in self.get_possible_moves():
            new_state = self.make_move(move)
            whole1 = new_state.row_marker + \
                     new_state.downleft_marker + new_state.downright_marker
            if whole1.count('1') >= (self.n * 3 + 3) / 2 or \
                    whole1.count('2') >= (self.n * 3 + 3) / 2:
                return 1
            for move1 in new_state.get_possible_moves():
                new_state1 = new_state.make_move(move1)
                whole2 = new_state1.row_marker \
                         + new_state1.downleft_marker \
                         + new_state1.downright_marker
                if whole2.count('1') >= (self.n * 3 + 3) / 2 or \
                        whole2.count('2') >= (self.n * 3 + 3) / 2:
                    result.append(-1)
                else:
                    result.append(1)
        if all([x == -1 for x in result]):
            return -1
        return sum([x for x in result]) / len(result)


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the StonehengeGame.
        """
        n = int(input("Enter the side-length n = "))
        list_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z']
        list_row = []
        count = 0
        for i in range(n):
            list_row.append(list_alpha[count: count + i + 2])
            count += i + 2
        list_row.append(list_alpha[count: count + n])
        self.current_state = StonehengeState(is_p1_turn, list_row, n)

    def __str__(self) -> str:
        """
        Return a string representing the StonehengeGame.
        """
        return "Let's play Stonehengegame!"

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff self is equal to other.
        """
        return type(self) == type(other) and \
               self.current_state == other.current_state

    def get_instructions(self) -> str:
        """
        Return the instructions for this StonehengeGame.
        """
        instructions = "GAME INSTRUCTIONS: Players take turns claiming cells" \
                       "(in the diagram: circles labelled with a capital " \
                       "letter).When a player captures at least half of the " \
                       "cells in a ley-line(in the diagram: hexagons with " \
                       "a line connecting it to cells), then the player " \
                       "captures that ley-line. The rst player to " \
                       "capture at least half of the ley-lines is the " \
                       "winner. A ley-line, once claimed, cannot be taken " \
                       "by the other player."
        return instructions

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not StonehengeGame is over at state.
        """
        whole = state.row_marker + state.downleft_marker \
                + state.downright_marker
        return whole.count('1') >= (state.n * 3 + 3) / 2 \
               or whole.count('2') >= (state.n * 3 + 3) / 2

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the StonehengeGame.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return string





if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
