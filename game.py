from __future__ import annotations
from typing import Optional, List, Tuple, Union
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
        start_pos:
            True if it is the start of the round, false while round is ongoing
        d_h:
            The display screens height
        d_w:
            The display screens width
        y_bound:
            The vertical [upper, lower] bounds of the moving actors(players and
                                                                     ball)
        x_bound:
            The horizontal [upper, lower] bounds of the moving actors(players
                                                                      and ball)
        self.upper_bound:
            The upper bar of the stage
        self.lower_bound:
            The lower bar of the stage

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
    start_pos: bool
    player1: HumanPlayer
    player2: Union[HumanPlayer, AIPlayer]
    ball: Ball
    _actors: List[Actor]
    d_w: int
    d_h: int
    y_bound: List[int]
    x_bound: List[int]
    board_player1: ScoreBoard
    board_player2: ScoreBoard
    start_message: Message
    pause_message: Message
    infinite_mode: bool


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
        self.upper_bound = None
        self.lower_bound = None
        self._actors = []
        self._pause = True
        self.d_w, self.d_h = pygame.display.get_surface().get_size()
        self.x_bound = [0, self.d_w]
        self.y_bound = None
        self.start_pos = True
        self.clock = pygame.time.Clock()
        self.infinite_mode = False
        self._game_begun = False
        self._new_round = True

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
            if actor_x < x < actor_x + actor_width and \
                    actor_y < y < actor_y + actor_height:
                return actor
        return None

    def set_goal(self, score: int):
        self.goal_score = score

    def increase_goal(self):
        if not self.infinite_mode:
            self.goal_score += 1

    def decrease_goal(self):
        if self.goal_score > 1 and not self.infinite_mode:
            self.goal_score -= 1

    def toggle_infinite(self):
        self.infinite_mode = not self.infinite_mode

    def set_pause(self, switch: bool) -> None:
        self._pause = switch

    def set_new_round(self, switch: bool) -> None:
        self._new_round = switch

    def game_won(self) -> bool:
        """
        Return True iff the game has been won.
        """
        if self.player1.get_score() == self.goal_score or \
                self.player2.get_score() == self.goal_score:
            return True
        return False

    def new_round(self):
        """
        Reset the stage for the new round. If this the beginning of the game,
        creat new players and ball, else just reset the position.
        """
        if self._game_begun is False:
            d_h, d_w = self.d_h, self.d_w
            h_bars = round(d_h * 0.05)
            self.y_bound = [h_bars, d_h - h_bars]
            self.player1 = HumanPlayer(10, (d_h // 2) - 40, self.y_bound, self)
            self.player2 = HumanPlayer(d_w - 25, (d_h // 2) - 40, self.y_bound, self)
            self.ball = Ball(d_w // 2, d_h // 2, self.y_bound, self.x_bound, self)

            self.upper_bound = Boundaries(0, 0, d_w, h_bars, self.y_bound, self)
            self.lower_bound = Boundaries(0, d_h - h_bars, d_w, h_bars,
                                          self.y_bound, self)

            self.board_player1 = ScoreBoard(d_w // 3, 450, 50, 50, 0,
                                            self.player1, self)
            self.board_player2 = ScoreBoard(2 * d_w // 3, 450, 50, 50, 0,
                                            self.player2, self)

            self.start_message = Message(d_w // 2, d_h // 2, 50, 50,
                                         0, self, "Press SPACE to start", True)
            self.pause_message = Message(d_w // 2, d_h // 2, 50, 50,
                                         0, self, "Game Paused - Press 'r' to resume", False)

            self._actors = []
            self._actors.extend([self.player1, self.player2, self.ball,
                                 self.upper_bound, self.lower_bound,
                                 self.board_player1, self.board_player2,
                                 self.start_message, self.pause_message])

        else:
            self.player1.reset_pos()
            self.player2.reset_pos()
            self.ball.reset_pos()
            self.start_message.set_drawn(True)


    def on_init(self) -> None:
        """
        Initialize this game.
        """
        self._running = True
        pygame.display.set_caption("PING")
        self.new_round()

    def on_move(self, dt: float) -> None:
        """
        Move every object on the stage while this game is on execute.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
        keys = pygame.key.get_pressed()

        #Case when a round is ongoing and is not paused
        if not self._pause and not self._new_round:
            # player1 moves
            if keys[pygame.K_p]:
                self._pause = True
                self.pause_message.set_drawn(True)
                return
            if keys[pygame.K_w] and (self.player1.get_coordinates()[1] -
                                     self.player1.get_speed() >= 0):
                self.player1.move("up", dt)
            if keys[pygame.K_s] and (self.player1.get_coordinates()[1] +
                                     self.player1.get_dimensions()[1] +
                                     self.player1.get_speed() <= 720):
                self.player1.move("down", dt)

            # player2 moves
            if keys[pygame.K_UP] and (self.player2.get_coordinates()[1] -
                                      self.player2.get_speed() >= 0):

                self.player2.move("up", dt)
            if keys[pygame.K_DOWN] and (self.player2.get_coordinates()[1] +
                                        self.player2.get_dimensions()[1] +
                                        self.player2.get_speed() <= 720):
                self.player2.move("down", dt)

            self.ball.move(dt)

        #Case when user has paused the game
        elif not self._new_round:
            if keys[pygame.K_r]:
                self._pause = False
                self.start_message.set_drawn(False)
                self.pause_message.set_drawn(False)
                self.ball.move(dt)

        #Case when its a new round
        else:
            if keys[pygame.K_SPACE]:
                self._game_begun = True
                self._new_round = False
                self._pause = False
                self.start_message.set_drawn(False)
                self.ball.init_move()

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """
        # set up the game
        self.on_init()
        # run the game
        while self._running:

            dt = self.clock.tick() / 30
            # print(self.clock.get_fps())
            # move objects on the stage
            self.on_move(dt)

            # show up changes on the screen
            self.screen.fill(BLACK)
            display_width, display_height = \
                pygame.display.get_surface().get_size()

            y = 6
            for i in range(0, 20):
                pygame.draw.rect(self.screen, WHITE, ((display_width//2)-1, y, 2, 24))
                y += 36

            for actor in self._actors:
                actor.draw()


            # Update ScoreBoards:
            self.board_player1.update()
            self.board_player2.update()
            # pygame.draw.rect(self.screen, RED, (0,0, display_width,5 ))
            pygame.display.update()

        pygame.quit()

