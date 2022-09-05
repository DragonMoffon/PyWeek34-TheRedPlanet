from src.enemies.ai import Ai
from src.enemies.enemy import Enemy
from src.enemies.data import Data


class DataGrunt(Data):

    def __init__(self, target):
        pass


class AiGrunt(Ai):

    def __init__(self):
        super().__init__()


class EnemyGrunt(Enemy):

    def __init__(self, manager):
        super().__init__(manager, AiGrunt())
        pass
