from src.enemies.ai import Ai


class Enemy:

    def __init__(self, manager, ai):
        self._manager = manager
        self._ai = ai

        self._renderer = None
