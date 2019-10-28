"""
This module initializes and runs the main game.
"""

from game import Game

SCREEN_SIZE = (960, 500)

if __name__ == "__main__":
    goal_score = 10
    game = Game(SCREEN_SIZE, goal_score)
    game.on_execute()
