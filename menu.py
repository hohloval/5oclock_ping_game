from __future__ import annotations
from typing import Optional, List, Callable
from game import Game
import pygame

class MainMenu:
    """
    The main menu that gives the user the option to: start a human vs human
    game, human vs AI game, change the settings, and exit the game
    """
    _buttons: List[_Button]
    _game: Game

    def __init__(self):
        """
        Initializes the menu and all of its buttons
        """

    def display(self):
        """
        Displays the menu to the player
        """

        # Interaction loop
        while True:
            self.draw_menu()
            # check for player input (loop through buttons)
            # if player clicks a button, run button.onClick

    def draw_menu(self):
        """
        Draws everything to the screen
        """


class _Button:
    """
    A button the user can click on to make something happen
    """
    x: int
    y: int
    width: int
    height: int
    on_click: Callable

    def __init__(self, x, y, width, height, on_click):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on_click = on_click

    def draw(self):
        """
        Draws the button to the screen
        """

