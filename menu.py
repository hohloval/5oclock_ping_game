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

    def __init__(self, game):
        """
        Initializes the menu and all of its buttons
        """
        self._game = game;
        self._buttons.append(_Button(400, 200, 100, 50,
                                     "Two player game", None))


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
        for (button in self._buttons):
            button.draw(self._game);


class _Button:
    """
    A button the user can click on to make something happen
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _label: str
    _on_click: Callable

    def __init__(self, x, y, width, height, label, on_click):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._label = label
        self._on_click = on_click

    def draw(self, game: Game):
        """
        Draws the button to the screen
        """

        # Useful colour name variables
        blue = pygame.Color((0, 0, 255))
        white = pygame.Color((255, 255, 255))

        # Setting up label text
        font = pygame.font.Font(None, 14)
        button_label = font.render(self._label, True, white)

        # Drawing to screen
        pygame.draw.rect(game.screen, blue, (self._x, self._y, self._width,
                                             self._height))
        game.screen.blit(button_label, (self._x, self._y))


