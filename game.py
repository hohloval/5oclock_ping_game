from __future__ import annotations
from typing import Optional, List
from actors import *
import pygame
import random


class Game:
    """
        This class represents the main game.

        === Public Attributes ===
        screen:
            The screen/stage for display in this game.
        screen_size:
            The size of the stage given by width x length (in pixels).
        goal_score:
            The goal score in this game.
        player1:
            The first player (human) in this game.
        player2:
            The second player (human OR AI) in this game.
        ball:
            The ball in this game.

        === Private Attributes ===
        _running:
            Whether or not the game is running.
        _actors:
            The list of all the Actor objects in this game.
        """
    screen: Surface
    screen_size: Tuple[int]
    _running: bool
    goal_score: int
    player1: HumanPlayer
    player2: Union[HumanPlayer, AIPlayer]
    ball: Ball
    _actors: List[Actor]

    def __init__(self, size: Tuple[int], goal: int) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """
        self.screen = pygame.display.set_mode(size)
        self.screen_size = size
        self._running = False
        self.goal_score = goal

        self.player1 = None
        self.player2 = None
        self.ball = None
        self._actors = []

    # TODO: Check if works properly.
    def get_actor(self, x: int, y: int) -> Optional[Actor]:
        """
        Return the actor object that exists in the location given by
        <x> and <y>. If no actor exists in that location, return None.
        """
        for actor in self._actors:
            actor_x, actor_y = actor.get_coordinates()[0], \
                               actor.get_coordinates()[1]
            actor_width, actor_height = actor.get_dimensions()[0], \
                                        actor.get_dimensions()[1]
            if x in range(actor_x, actor_x + actor_width + 1) and \
                    y in range(actor_y, actor_y + actor_height + 1):
                return actor
        return None

    def game_won(self) -> bool:
        """
        Return True iff the game has been won.
        """
        if self.player1.get_score() == self.goal_score or \
                self.player2.get_score() == self.goal_score:
            return True
        return False

    def on_init(self) -> None:
        """
        Initialize this game.
        """
        pygame.init()
        self._running = True
        pygame.display.set_caption("PING")

        display_width, display_height = pygame.display.get_surface().get_size()

        self.player1 = HumanPlayer(10, 0)
        self.player2 = HumanPlayer(935, 0)
        self.ball = Ball(display_width//2, display_height//2)
        self._actors.extend([self.player1, self.player2, self.ball])

    def on_move(self) -> None:
        """
        Move every object on the stage while this game is on execute.
        """
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
        keys = pygame.key.get_pressed()

        # player1 moves
        if keys[pygame.K_w] and (self.player1.get_coordinates()[1] -
                                 self.player1.get_speed() >= 0):
            self.player1.move("up")
        if keys[pygame.K_s] and (self.player1.get_coordinates()[1] +
                                 self.player1.get_dimensions()[1] +
                                 self.player1.get_speed() <= 720):
            self.player1.move("down")

        # player2 moves
        if keys[pygame.K_UP] and (self.player2.get_coordinates()[1] -
                                  self.player2.get_speed() >= 0):
            self.player2.move("up")
        if keys[pygame.K_DOWN] and (self.player2.get_coordinates()[1] +
                                    self.player2.get_dimensions()[1] +
                                    self.player2.get_speed() <= 720):
            self.player2.move("down")

        # ball moves
        self.ball.move(self)

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """
        # set up the game
        self.on_init()

        # run the game
        while self._running:

            # move objects on the stage
            self.on_move()

            # show up changes on the screen
            self.screen.fill(BLACK)

            y = 6
            for i in range(0, 20):
                pygame.draw.rect(self.screen, WHITE, (479, y, 2, 24))
                y += 36

            for actor in self._actors:
                actor.draw(self)
            pygame.display.update()

        pygame.quit()

    def main_menu(self):
        """
        Displays the main menu which allows the user to start a game,
        change settings, and exit the game.
        """
        return

