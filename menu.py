from __future__ import annotations
from typing import Optional, List, Callable
from game import Game
from button import Button
import pygame
from high_score import HighScore

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
    _surface: pygame.Surface
    _high_score: HighScore

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
        h_s_width = 5*(self._surface.get_width()) // 6
        h_s_height = self._surface.get_height() // 4
        self._high_score = HighScore(h_s_width, h_s_height, 70, (250, 250, 250),
                                     self._surface, "high_score_value.txt")

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

        self._high_score.draw()

        if self._game.infinite_mode:
            font = pygame.font.Font(None, 28)
            goal_label = font.render("infinite", True, white)
            self._surface.blit(goal_label, (mid_pos[0] - 120, mid_pos[1] + 80))
        else:
            font = pygame.font.Font(None, 36)
            goal_label = font.render(str(self._game.goal_score), True, white)
            self._surface.blit(goal_label, (mid_pos[0]-80, mid_pos[1]+80))
