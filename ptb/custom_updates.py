from dataclasses import dataclass


@dataclass
class CustomUpdate:
    """Simple dataclass to wrap a custom update type"""

    user_id: int
    payload: str
