import math

import pygame

from UI import UI


def main():
    # Démmarre le module
    pygame.init()

    ui = UI()
    running = True
    score = 0
    moon_angle = -math.pi / 2
    button_clicking = False

    ui.display_init()

    # Boucle de l'animation
    while running:
        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(score)

        # Clic bouton fuëlle
        if pygame.mouse.get_pressed()[0]:
            if ui.check_mouse_position_fuelle_button() and not button_clicking:
                ui.display_button_down()
                score += 1
            button_clicking = True
        else:
            ui.display_button_up()
            button_clicking = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        pygame.display.update()

if __name__ == '__main__':
    main()
