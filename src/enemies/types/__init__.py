from src.enemies.types.grunt import Grunt, GruntData

TYPES = ((GruntData, Grunt),)
ENEMIES = {data.name: enemy for data, enemy in TYPES}


def valid_enemies(thresh):
    return [GruntData.name]
