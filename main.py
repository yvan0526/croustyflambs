import math

import pygame

from UI import UI


def main():
    # Démmarre le module
    pygame.init()

    ui = UI()
    running = True
    score = 100

    # Boucle de l'animation
    while running:
        # Texte score
        ui.display_score(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Incrémente lors d'un clic sur le bouton
                if ui.check_mouse_click_fuelle_button():
                    score += 1
                    ui.display_button_down()
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
