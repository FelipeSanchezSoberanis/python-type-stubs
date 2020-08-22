from typing import AnyStr, Sequence

def init() -> None: ...
def get_init() -> bool: ...
def get(data_type: str) -> AnyStr: ...
def get_types() -> Sequence[str]: ...
def put(data_type: str, data: AnyStr) -> None: ...
def contains(data_type: str) -> bool: ...
def lost() -> bool: ...
def set_mode(mode: int) -> None: ...
