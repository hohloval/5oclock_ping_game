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

        mid_pos = (size[0] // 2, size[1] // 2)
        self._buttons = [Button(mid_pos[0] - 100, mid_pos[1] - 50, red, 200,
                                 70, "Two player game", game.on_execute)]
        # choose point limit

        self._buttons.append(Button(mid_pos[0] + 20, mid_pos[1] + 50, red, 30,
                                    30, "Up", game.increase_goal))
        self._buttons.append(Button(mid_pos[0] + 60, mid_pos[1] + 50, red, 50,
                                    30, "Down", game.decrease_goal))
        self._buttons.append(Button(mid_pos[0] - 10, mid_pos[1] + 90, red, 120,
                                    30, "Infinite mode", game.toggle_infinite))

        # display high scores

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
                        if button.check_mouse_pos(mouse_x, mouse_y):
                            button.on_click()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def draw_menu(self):
        """
        Draws everything to the screen
        """
        size = self._surface.get_size()
        mid_pos = (size[0] // 2, size[1] // 2)

        self._surface.fill(black)

        for button in self._buttons:
            button.draw(self._surface)

        font = pygame.font.Font(None, 108)
        title = font.render("P I N G", True, white)
        self._surface.blit(title, (mid_pos[0] - title.get_size()[0]//2, 70))

        font = pygame.font.Font(None, 28)
        goal_label = font.render("Score Limit", True, white)
        self._surface.blit(goal_label, (mid_pos[0] - 120, mid_pos[1] + 60))

        # get goal score
        limit = self._game.goal_score
        if limit == 0:
            font = pygame.font.Font(None, 28)
            goal_label = font.render("infinite", True, white)
            self._surface.blit(goal_label, (mid_pos[0] - 120, mid_pos[1] + 80))
        else:
            font = pygame.font.Font(None, 36)
            goal_label = font.render(str(limit), True, white)
            self._surface.blit(goal_label, (mid_pos[0]-80, mid_pos[1]+80))


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
