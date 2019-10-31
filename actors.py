from __future__ import annotations
import pygame
import random
# from game import Game
from typing import Optional, Tuple, Union

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Actor:
    """
    A class to represent all the game's actors. This class includes any
    attributes/methods that every actor in the game must have.

    This is an abstract class. Only subclasses should be instantiated.

    === Private Attributes ===
    _x:
        x coordinate of this actor's location on the stage
    _y:
        y coordinate of this actor's location on the stage
    _dx:
        Change in x coordinate per unit of time
    _dy:
        Change in y coordinate per unit of time
    _width:
        width of this actor
    _height:
        height of this actor
    _color:
        color of this actor
    _speed:
        speed of this actor
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]
    _speed: int

    def __init__(self, x, y, width, height, y_bound, game):
        """
        Initialize an actor with the given <x> and <y> position and
        <width>x<height> dimensions on the game's stage.
        """
        self._x, self._y, self._width, self._height = x, y, width, height
        self._color = WHITE
        self.y_bound = y_bound
        self.game = game

    def move(self, dt: float) -> None:
        """
        Move this actor.
        """

        raise NotImplementedError

    def draw(self) -> None:
        """
        Draw this actor on the stage.
        """
        pygame.draw.rect(self.game.screen, self._color, (int(self._x), int(self._y),
                                                    self._width, self._height))

    def get_coordinates(self) -> Tuple[int, int]:
        """
        Return the coordinates of this actor.
        """
        return self._x, self._y

    def get_dimensions(self) -> Tuple[int, int]:
        """
        Return the dimensions of this actor.
        """
        return self._width, self._height

    def get_speed(self) -> int:
        """
        Return the speed of this actor.
        """
        return self._speed


class HumanPlayer(Actor):
    """
    A class to represent a Human Player in the game.

    === Private Attributes ===
    _score:
        score of this human player
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]
    _speed: int
    _score: int

    def __init__(self, x: int, y: int, y_bound, game: 'Game') -> None:
        """
        Initialize a HumanPlayer at the position <x> and <y> on the stage.
        """
        super().__init__(x, y, 15, 80, y_bound, game)
        self._speed = 10
        self._score = 0

    def reset_pos(self) -> None:
        """
        Set the position of the bar by changing the self._x and self._y values.
        """
        self._y = (self.game.d_h//2) - 40

    def get_score(self) -> int:
        """
        Return the score of this human player.
        """

        return self._score

    def move(self, direction: str, dt: float) -> None:
        """
        Move the human player on the <game>'s stage based on direction.
        """
        if (direction == "up") and (self._y-self._speed) >= self.y_bound[0]:
            self._y -= self._speed * dt
        elif (direction == "down") and ((self._y+self._height)+self._speed)<=self.y_bound[1]:
            self._y += self._speed * dt

    def change_score(self, change_in_score: int):
        self._score += change_in_score



class AIPlayer(Actor):
    """
    A class to represent an AI Player in the game.

    === Private Attributes ===
    _score:
        score of this AI player
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]
    _speed: int
    _score: int

    def __init__(self, x: int, y: int, game: 'Game') -> None:
        """
        Initialize an AI Player at the position <x> and <y> on the stage.
        """

        super().__init__(x, y, 10, 10, game)
        self.velocity = 10

    def get_score(self) -> int:
        """
        Return the score for this AI player.
        """

        return self._score

    # TODO: implement
    def move(self) -> None:
        """
        Move the player on the <game>'s stage.
        """
        pass


class Ball(Actor):
    """
    A class to represent a Ball in the game.
    """
    _x: int
    _y: int
    _dx: int
    _dy: int
    _width: int
    _height: int
    _color: str

    def __init__(self, x: int, y: int, y_bound: list[int] , x_bound: list[int], game: 'Game') -> None:
        """
        Initialize a ball with the given x and y position
        """
        super().__init__(x, y, 18, 18, y_bound, game)
        self._color = RED
        # self._range_of_dx = range(-4,4)
        # self._range_of_dy = range(-4,4)
        self._dx = None
        self._dy = None
        self.x_bound = x_bound

    def draw(self) -> None:
        """
        Draws the ball to the screen.
        """
        pygame.draw.circle(self.game.screen, self._color, (int(self._x), int(self._y)),
                           self._width)
    # TODO: implement

    def move(self, dt: float) -> None:
        """
        Move the ball on the <game>'s stage based.
        """
        new_x = self._x+self._dx
        new_y = self._y+self._dy

        check_collision = self.check_collision(new_x, new_y)

        # Check collision with Top border
        if new_y - self._width <= self.y_bound[0]:
            self._x += self._dx * dt
            self._y = self.y_bound[0]+self._height
            self._dy = -self._dy
            return

        # Check Collision with bottom Border
        elif new_y + self._width >= self.y_bound[1]:
            self._x += self._dx * dt
            self._y = self.y_bound[1]-self._height
            self._dy = -self._dy
            return
            # Check collision with paddles
        elif self.check_collision(new_x, new_y):
            self._x = new_x
            self._y = new_y
            self._dx = -self._dx

            # check if the ball is coming up or coming down
            if self._dy > 0:
                self._dy = self.new_direction(-16, 0)[1]
            elif self._dy < 0:
                self._dy = self.new_direction(0, 16)[1]
            else:
                self._dy = self.new_direction(-16, 16)[1]

        # Check Collision with left screen edge
        elif new_x - self._width <= self.x_bound[0]:
            self.game.player2.change_score(1)
            self.game.new_round()
            self.game.set_go(False)
            return

        # Check Collision with right screen edge
        elif new_x + self._width >= self.x_bound[1]:
            self.game.player1.change_score(1)
            self.game.new_round()
            self.game.set_go(False)
            return

        # Check Collision with right paddle
        # coords = game.player2.get_coordinates()
        # dims = game.player2.get_dimensions()
        # mid_y = (new_y + dims[1]) // 2 + new_y
        # if new_x + self._width > coords[0] and coords[1] < mid_y < coords[1] - dims[0]:
        #     self._dx = -self._dx
        #     self._x = coords[0] + self._width
        #     self._y += self._dy

        # No Collision
        else:
            self._x += self._dx * dt
            self._y += self._dy * dt

    def check_collision(self, new_x: int, new_y: int):
        """
        Checks if the ball collides with a paddle and returns [True/False, pos
        of collision]
        """
        if self._dx > 0:
            for i in range(-self._height, self._height):
                if isinstance(self.game.get_actor(new_x + self._width, new_y + i),
                           HumanPlayer):
                    return True
            return False
        else:
            for i in range(-self._height, self._height):
                if isinstance(self.game.get_actor(new_x - self._width, new_y + i),
                           HumanPlayer):
                    return True
            return False

    def reset_pos(self):
        """
        Resets the position of the ball for a new round.
        """
        self._x = self.game.d_w//2
        self._y = self.game.d_h//2

    def init_move(self) -> None:
        """
        Is the initial movement of the ball at the beginning of the round.
        """
        self._dy = self.new_direction(-16, 16)[1]
        self._dx = random.choice([-10, 10])

    def new_direction(self, lower: int, upper: int) -> Tuple[int, int]:
        """
        Calculates a randomized direction of movement for the ball, that is
        dx and dy.

        lower: The lower bound for the change in y direction
        upper: the upper bound for the change in the y direction
        return a tuple containing x, and y coordinates for the new direction
        """
        y = random.randint(lower, upper)
        x = 10
        # if x in range(-1, 1):
        #     x = 2
        return x, y


class Boundaries(Actor):
    """
    Class represents the upper and lower boundaries of the stage.
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]

    def __init__(self, x: int, y: int, width: int, height: int, y_bound: list[int], game:'Game' ) ->None:
        super().__init__(x, y, width, height, y_bound, game)
        self._color = RED

    def draw(self) -> None:
        """
        Draws the ball to the screen.
        """
        pygame.draw.rect(self.game.screen, self._color, (self._x, self._y,
                                                    self._width, self._height))

    def move(self):
        return


class Message(Actor):
    """
    A Message of text that displays on the game screen
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]
    _speed: int
    _text: str
    _is_drawn: bool

    def __init__(self, x, y, width, height, y_bound, game, text, is_shown):
        """
        Initialize an actor with the given <x> and <y> position and
        <width>x<height> dimensions on the game's stage.
        """
        super().__init__(x, y, width, height, y_bound, game)
        self._color = (81, 194, 231)
        self.y_bound = y_bound
        self.game = game
        self._text = text
        self._is_drawn = is_shown

    def set_drawn(self, cond: bool):
        """
        Sets this text to be drawn, or not based on the condition

        cond: the condition on whether this object is displayed
        """
        self._is_drawn = cond

    def draw(self):
        """
        Draw the text to the screen if the message is supposed to
        be drawn
        """
        if self._is_drawn:
            font = pygame.font.Font(None, 70)
            text = font.render(self._text, 1, self._color)
            text_pos = text.get_rect(centerx=self._x, centery=self._y)
            self.game.screen.blit(text, text_pos)

    def move(self):
        """
        This actor cannot be moved
        """
        pass


class ScoreBoard(Actor):
    """
    Represents the Scoreboard of one player in the game
    """

    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]
    _score: int
    _player: Union[HumanPlayer, AIPlayer]

    def __init__(self, x: int, y: int, width: int, height: int, y_bound,
                 player: Union[HumanPlayer, AIPlayer], game:'Game') -> None:
        super().__init__(x, y, width, height, y_bound, game)
        self._color = WHITE
        self._score = 0
        self._player = player

    def draw(self) -> None:
        """
        Draws the score to the screen.
        """
        font = pygame.font.Font(None, 70)
        text = font.render(str(self._score), 1, self._color)
        text_pos = text.get_rect(centerx=self._x, centery=self._y)
        self.game.screen.blit(text, text_pos)

    def move(self):
        return

    def update(self):
        """
        Updates the score value of this object with the corresponding score
        value in the game
        """
        self._score = self._player.get_score()
