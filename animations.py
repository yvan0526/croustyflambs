import math

from animation import Animation
from src.modele.etat import Etat


def get_end_animation(ui, score):
    percent = math.log10(min(score / Etat.SCORE_GOAL, 1) * 240 + 1) / math.log10(241) * 100
    if score < 1:
        return Animation(ui.screen, ui.end_blanchon_images, 364, 84)
    elif percent < 40:
        return Animation(ui.screen, ui.end_iut_images, 220, 20)
    elif percent < 44:
        return Animation(ui.screen, ui.end_happy_images, 220, 20)
    elif percent < 100:
        return Animation(ui.screen, ui.end_luniens_images, 220, 20)
    elif percent <= 105:
        return Animation(ui.screen, ui.end_100_images, 220, 20)
    elif percent > 105:
        return Animation(ui.screen, ui.end_sun_images, 220, 20)
    else:
        return Animation(ui.screen, ui.end_iut_images, 220, 20)
