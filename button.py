from __future__ import annotations
from typing import Callable
import pygame

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)


class Button:
    """
    A button the user can click on to make something happen
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _label: str
    on_click: Callable
    white = (250, 250, 250)

    def __init__(self, x: int, y: int, colour: tuple, width: int, height: int,
                 label: str, on_click: Callable):
        self._x = x
        self._y = y
        self.colour = colour
        self._width = width
        self._height = height
        self._label = label
        self.on_click = on_click

    def check_mouse_pos(self, mouse_x: int, mouse_y: int):
        """
        Checks if the mouse click is on this button.
        :return boolean
        """
        return (self._x <= mouse_x <= self._x + self._width) and \
               (self._y <= mouse_y <= self._y + self._height)

    def draw(self, surface: Surface):
        """
        Draws the button to the screen
        """

        # Setting up label text
        font = pygame.font.Font(None, 24)
        button_label = font.render(self._label, True, white)
        label_size = button_label.get_size()
        offset_x = (self._width - label_size[0])//2
        offset_y = (self._height - label_size[1])//2

        # Drawing button to screen
        pygame.draw.rect(surface, self.colour, (self._x, self._y, self._width,
                                                self._height))
        # Draw label centered in button
        surface.blit(button_label, (self._x + offset_x,
                                    self._y + offset_y))

    def get_rect(self) -> pygame.rect.Rect:
        """
        Retrieves a pygame.Rect object of this button
        :return: a pygame.Rect object corresponding to the size/position
         of this button
        """
        return pygame.rect.Rect(self._x, self._y, self._width, self._height)
