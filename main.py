import math

import pygame

def main():
    # Démmarre le module
    pygame.init()
    # définit l'écran et sa taille, retourne la surface pour le dessin
    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
    # Pour savoir quand la boucle du jeu se termine
    running = True

    font = pygame.font.SysFont(None, 80)
    nb_click = 0

    # Boucle de l'animation
    while running:
        # Couleur de fond
        screen.fill("gray")

        # Texte
        text = font.render(f"{nb_click}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = ((int)(screen.get_width() / 2), (int)(screen.get_height() / 2 - 250))
        screen.blit(text, text_rect)

        # Bouton
        button_rect = pygame.Rect(screen.get_width() / 2 - 50, screen.get_height() / 2 - 50, 100, 100)
        pygame.draw.rect(screen, "red", button_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Incrémente lors d'un clic sur le bouton
                if (button_rect.left < pygame.mouse.get_pos()[0] < button_rect.right
                        and button_rect.top < pygame.mouse.get_pos()[1] < button_rect.bottom):
                    nb_click += 1

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        pygame.display.update()

if __name__ == '__main__':
    main()
