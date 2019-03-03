"""
3x3 Tile Problem

Initial State: 7245_6831
Goal State: 12345678_

"""

import search_uniformcost_greedy_astar as alg
from utils import distance
infinity = float('inf')


class TileProblem(alg.Problem):

    legalMoves = (
        (1, 3),
        (0, 4, 2),
        (1, 5),
        (0, 4, 6),
        (1, 3, 5, 7),
        (2, 4, 8),
        (3, 7),
        (4, 6, 8),
        (5, 7)
    )

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.explored = {}
        self.manhattan_dist = {}

        for a in range(9):
            for b in range(9):
                a_row = a / 3
                a_col = a % 3

                b_row = b / 3
                b_col = b % 3

                self.manhattan_dist[(a, b)] = abs(a_row - b_row) + abs(a_col - b_col)

    def h(self, n):
        result = 0

        for a in range(9):
            for b in range(9):
                result += self.manhattan_dist[(a, b)]

        return result

    def actions(self, current_board):
        empty_pos = current_board.find('_')
        actions = []

        for mov in self.legalMoves[empty_pos]:
            actions.append(mov)

        return actions

    def result(self, current_board, action):
        empty_pos = current_board.find('_')
        board = list(current_board)

        board[empty_pos], board[action] = board[action], board[empty_pos]
        return "".join(board)

    def path_cost(self, c, state1, action, state2):
        cost = 0
        for square in range(9):
            occupant = state1[square]
            if occupant != '_':
                wanted_goal = self.goal.find(occupant)
                cost += self.manhattan_dist[(square, wanted_goal)]

        return cost


initial = "7245_6831"
goal = "12345678_"
tile_board = TileProblem(initial, goal)
#print(alg.uniform_cost_search(tile_board))
print(alg.greedy_best_first_graph_search(tile_board))
#print(alg.astar_search(tile_board))

