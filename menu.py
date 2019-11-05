from __future__ import annotations
from typing import Optional, List, Callable
from game import Game
import pygame

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)


class MainMenu:
    """
    The main menu that gives the user the option to: start a human vs human
    game, human vs AI game, change the settings, and exit the game
    """
    _buttons: List[_Button]
    _game: Game
    _surface: Surface

    def __init__(self, game, size):
        """
        Initializes the menu and all of its buttons
        """
        self._surface = pygame.display.set_mode(size)
        self._game = game
        self._buttons = [_Button(400, 200, 100, 50, "Two player game",
                                 game.on_execute)]

    def display(self):
        """
        Displays the menu to the player
        """

        # Interaction loop
        while True:
            pygame.display.update()
            self.draw_menu()
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Check if mouse has clicked any buttons
                    for button in self._buttons:
                        if button.check_mouse_click(mouse_x, mouse_y):
                            button.on_click()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def draw_menu(self):
        """
        Draws everything to the screen
        """
        self._surface.fill(black)
        for button in self._buttons:
            button.draw(self._surface)


class _Button:
    """
    A button the user can click on to make something happen
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _label: str
    on_click: Callable

    def __init__(self, x, y, width, height, label, on_click):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._label = label
        self.on_click = on_click

    def check_mouse_click(self, mouse_x: int, mouse_y: int):
        """
        Checks if the mouse click is on this button.
        """
        return (self._x <= mouse_x <= self._x + self._width) and \
               (self._y <= mouse_y <= self._y + self._height)

    def draw(self, surface: Surface):
        """
        Draws the button to the screen
        """

        # Setting up label text
        font = pygame.font.Font(None, 14)
        button_label = font.render(self._label, True, white)

        # Drawing to screen
        pygame.draw.rect(surface, red, (self._x, self._y, self._width,
                                         self._height))
        surface.blit(button_label, (self._x, self._y))
