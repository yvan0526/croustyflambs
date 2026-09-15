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

    # Boucle de l'animation
    while running:
        # Affiche la Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

        # Affiche la progress bar
        ui.display_progress_bar(score, 100)

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(score)

        # Clic bouton fuëlle
        if pygame.mouse.get_pressed()[0]:
            if ui.check_mouse_position_fuelle_button() and not button_clicking:
                score += 1
            ui.display_button_down()
            button_clicking = True
        else:
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
