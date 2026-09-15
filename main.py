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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Clic bouton fuëlle
                if ui.check_mouse_position_fuelle_button():
                    ui.display_button_down()
                    score += 1
            elif event.type == pygame.MOUSEBUTTONUP:
                ui.display_button_up()

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        pygame.display.update()

if __name__ == '__main__':
    main()
