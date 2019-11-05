"""
This module initializes and runs the main game.
"""

from game import Game
from menu import MainMenu
import pygame

SCREEN_SIZE = (960, 500)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("PING")

    goal_score = 10
    game = Game(SCREEN_SIZE, goal_score)
    mainMenu = MainMenu(game, SCREEN_SIZE)
    mainMenu.display()
