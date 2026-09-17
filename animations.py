from animation import Animation


def get_end_animation(ui, score):
    if score < 1:
        return Animation(ui.screen, ui.end_blanchon_images, 364, 84)
    elif score < 400000000000000:
        return Animation(ui.screen, ui.end_iut_images, 220, 20)
    elif score < 440000000000000:
        return Animation(ui.screen, ui.end_happy_images, 220, 20)
    elif score < 950000000000000:
        return Animation(ui.screen, ui.end_luniens_images, 220, 20)
    elif score <= 1050000000000000:
        return Animation(ui.screen, ui.end_100_images, 220, 20)
    elif score > 1050000000000000:
        return Animation(ui.screen, ui.end_sun_images, 220, 20)
    else:
        return Animation(ui.screen, ui.end_iut_images, 220, 20)
