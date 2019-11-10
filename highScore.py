from typing import Tuple
import game


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
    _game: Game
    _score_file: str
    _high_score: int

    def __init__(self, center_x: int, center_y: int, font_size: int,
                 color: Tuple, curr_game: Game, score_file: str):
        self. _center_x = center_x
        self._center_y = center_y
        self._color = color
        self._font_size = font_size
        self._game = curr_game
        self._score_file = score_file
        self._get_score()

    #TODO: implement this method
    def draw(self) -> None:
        """
        Draw the high score onto the game screen
        """

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
            self._high_score = file.readline()
