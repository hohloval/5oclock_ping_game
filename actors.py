from __future__ import annotations
import pygame
from typing import Optional

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

    def __init__(self, x, y, width, height):
        """
        Initialize an actor with the given <x> and <y> position and
        <width>x<height> dimensions on the game's stage.
        """
        self._x, self._y, self._width, self._height = x, y, width, height
        self._color = WHITE

    def move(self, game: Game) -> None:
        """
        Move this actor.
        """

        raise NotImplementedError

    def draw(self, game: Game) -> None:
        """
        Draw this actor on the stage.
        """
        pygame.draw.rect(game.screen, self._color, (self._x, self._y,
                                                    self._width, self._height))

    def get_coordinates(self) -> Tuple[int]:
        """
        Return the coordinates of this actor.
        """
        return self._x, self._y

    def get_dimensions(self) -> Tuple[int]:
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

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a HumanPlayer at the position <x> and <y> on the stage.
        """

        super().__init__(x, y, 15, 80)
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
        if direction == "up":
            self._y -= self._speed
        elif direction == "down":
            self._y += self._speed


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
    def move(self, game: Game) -> None:
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
    _width: int
    _height: int
    _color: str
    _speed: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a ball with the given x and y position
        """
        super().__init__(x, y, 18, 18)
        self._color = RED

    def draw(self, game: Game) -> None:
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
        pass