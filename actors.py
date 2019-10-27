from __future__ import annotations
import pygame
import random
# from game import Game
from typing import Optional, Tuple

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

    def __init__(self, x, y, width, height, y_bound):
        """
        Initialize an actor with the given <x> and <y> position and
        <width>x<height> dimensions on the game's stage.
        """
        self._x, self._y, self._width, self._height = x, y, width, height
        self._color = WHITE
        self.y_bound = y_bound

    def move(self, game: 'Game') -> None:
        """
        Move this actor.
        """

        raise NotImplementedError

    def draw(self, game: 'Game') -> None:
        """
        Draw this actor on the stage.
        """
        pygame.draw.rect(game.screen, self._color, (self._x, self._y,
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

    def __init__(self, x: int, y: int, y_bound) -> None:
        """
        Initialize a HumanPlayer at the position <x> and <y> on the stage.
        """

        super().__init__(x, y, 15, 80, y_bound)
        self._speed = 10
        self._score = 0

    def get_score(self) -> int:
        """
        Return the score of this human player.
        """

        return self._score

    def move(self, direction: str) -> None:
        """
        Move the human player on the <game>'s stage based on direction.
        """
        if (direction == "up") and (self._y-self._speed)>=self.y_bound[0]:
            self._y -= self._speed
        elif (direction == "down") and ((self._y+self._height)+self._speed)<=self.y_bound[1]:
            self._y += self._speed

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

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize an AI Player at the position <x> and <y> on the stage.
        """

        super().__init__(x, y, 10, 10)
        self.velocity = 10

    def get_score(self) -> int:
        """
        Return the score for this AI player.
        """

        return self._score

    # TODO: implement
    def move(self, game: 'Game') -> None:
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

    def __init__(self, x: int, y: int, y_bound, x_bound) -> None:
        """
        Initialize a ball with the given x and y position
        """
        super().__init__(x, y, 18, 18, y_bound)
        self._color = RED
        # self._range_of_dx = range(-4,4)
        # self._range_of_dy = range(-4,4)
        self._dx = None
        self._dy = None
        self.x_bound = x_bound

    def draw(self, game: 'Game') -> None:
        """
        Draws the ball to the screen.
        """
        pygame.draw.circle(game.screen, self._color, (self._x, self._y),
                           self._width)
    # TODO: implement

    def move(self, game: 'Game') -> None:
        """
        Move the ball on the <game>'s stage based.
        """
        new_x = self._x+self._dx
        new_y = self._y+self._dy
        if new_y - self._width <= self.y_bound[0]:
            self._x += self._dx
            self._y = self.y_bound[0]+self._width
            self._dy = -self._dy
        elif new_y + self._width >= self.y_bound[1]:
            self._x += self._dx
            self._y = self.y_bound[1]-self._width
            self._dy = -self._dy
        if new_x - self._width <= self.x_bound[0]:
            game.player2.change_score(1)
            self._x = game.d_w//2
            self._y = game.d_h//2
            game.set_go(False)
        elif new_x + self._width >= self.x_bound[1]:
            game.player1.change_score(1)
            self._x = game.d_w//2
            self._y = game.d_h//2
            game.set_go(False)
        if isinstance(game.get_actor(new_x, new_y), HumanPlayer):
            self._x += self._dx  # Have to randomise the x-axis movement
            self._y += self._dy
            self._dx = -self._dx
        else:
            self._x += self._dx
            self._y += self._dy

    def init_move(self, game: 'Game') -> None:
        """
        Is the initial movement of the ball at the beginning of the round.
        """
        self._dx = self.new_direction("x")
        self._dy = self.new_direction("y")

    def new_direction(self, axis: str) -> int:
        if axis == "x":
            x = random.randint(-5, 5)
            while x == 0:
                x = random.randint(-5, 5)
            return x
        elif axis == "y":
            y = random.randint(-5, 5)
            return y


class Boundaries(Actor):
    """
    Class represents the upper and lower boundaries of the stage.
    """
    _x: int
    _y: int
    _width: int
    _height: int
    _color: Tuple[int]

    def __init__(self, x: int, y: int, width: int, height: int, y_bound) ->None:
        super().__init__(x, y, width , height, y_bound )
        self._color = RED

    def draw(self, game: 'Game') -> None:
        """
        Draws the ball to the screen.
        """
        pygame.draw.rect(game.screen, self._color, (self._x, self._y,
                                                    self._width, self._height))

    def move(self, game: 'Game'):
        return


