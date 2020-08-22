from typing import Optional, Sequence, Tuple, Union

from pygame.math import Vector2
from pygame.rect import Rect

_Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
_RectValue = Union[
    Rect, Union[Tuple[int, int, int, int], Sequence[int]], Union[Tuple[_Coordinate, _Coordinate], Sequence[_Coordinate]],
]

def get_focused() -> bool: ...
def get_pressed() -> Sequence[bool]: ...
def get_mods() -> int: ...
def set_mods() -> int: ...
def set_repeat(delay: Optional[int] = ..., interval: Optional[int] = ...) -> None: ...
def get_repeat() -> Tuple[int, int]: ...
def name(key: int) -> str: ...
def key_code(name: str) -> int: ...
def start_text_input() -> None: ...
def stop_text_input() -> None: ...
def set_text_input_rect(rect: _RectValue) -> None: ...
