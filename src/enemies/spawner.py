from random import randint, randrange, choice


from src.enemies.types import valid_enemies


def generate_round(diff, thresh):
    possible_enemies = valid_enemies(thresh)

    next_waves = []
    while diff > 0:
        wave = []
        for _ in range(randint(4, 8)):
            e_type = choice(possible_enemies)
            wave.append(e_type)
            diff -= 1
            if diff < 0:
                break
        next_waves.append(wave)

    return next_waves
