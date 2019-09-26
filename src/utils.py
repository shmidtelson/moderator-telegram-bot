from __future__ import annotations
from typing import Optional

class BotMeta(type):
    _instance: Optional[Bot] = None

    def __call__(self) -> Bot:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
