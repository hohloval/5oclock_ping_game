from typing import Tuple
from game import Game
import pygame


class HighScore:
    """
    An object which displays and tracks the highest overall score.
    _center_x: The x coordinate of the center of the object
    _center_y: The y coordinate of the center of the object
    _font_size: The size of the font
    _color: A RGB tuple
    _game: The game this high score is to be displayed in
    _score_file: A string representation of a file path where the high score is
        stored.
    _high_score: An int representation of the high score
    """
    _center_x: int
    _center_y: int
    _font_size: int
    _color: Tuple[int, int, int]
    _surface: pygame.Surface
    _score_file: str
    _high_score: int

    def __init__(self, center_x: int, center_y: int, font_size: int,
                 color: Tuple, curr_surface: pygame.Surface, score_file: str):
        self._center_x = center_x
        self._center_y = center_y
        self._color = color
        self._font_size = font_size
        self._surface = curr_surface
        self._score_file = score_file
        self._get_score()

    def draw(self) -> None:
        """
        Draw the high score onto the game screen
        """
        font = pygame.font.Font(None, self._font_size)
        text = font.render("High Score", 1, self._color)
        text_pos = text.get_rect(centerx=self._center_x,
                                 centery=self._center_y - 35)

        font = pygame.font.Font(None, 70)
        text2 = font.render(str(self._high_score), 1, self._color)
        text2_pos = text2.get_rect(centerx=self._center_x,
                                   centery=self._center_y + 45)

        self._surface.blit(text2, text2_pos)
        pygame.draw.rect(self._surface, self._color,
                         (self._center_x - text.get_width()//2, self._center_y,
                          text.get_width(), 10))
        self._surface.blit(text, text_pos)

    #TODO: check if this method works
    def store_score(self, score) -> None:
        """
        Store the given score in the file by over-riding the old file with
        the new score.
        :param score: an int representing the score
        """
        with open(self._score_file, 'w') as file:
            file.write(score)

    #TODO: check if this method works
    def _get_score(self) -> None:
        """
        Gets the current high score from the file and sets
        self._high_score to it.
        """
        with open(self._score_file, 'r') as file:
            self._high_score = file.readline().rstrip()
