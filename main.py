import math

import pygame

def main():
    # Démmarre le module
    pygame.init()
    # définit l'écran et sa taille, retourne la surface pour le dessin
    screen = pygame.display.set_mode((640, 360))


    # Pour savoir quand la boucle du jeu se termine
    running = True

    clock = pygame.time.Clock()
    dt: int = 0
    t: int = 0

    font = pygame.font.SysFont(None, 80)
    nb_click = 0

    hasFirstUp: bool = False
    firstUpTime: int = -1
    nbAutoClicks: int = 0

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt
        if (t - firstUpTime) / 1000 > nbAutoClicks and hasFirstUp:
            nb_click += 1
            nbAutoClicks += 1

        # Couleur de fond
        screen.fill("gray")

        # Texte
        text = font.render(f"{nb_click}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = ((int)(screen.get_width() / 2), (int)(screen.get_height() / 2 - 100))
        screen.blit(text, text_rect)

        # Bouton principal
        button_rect = pygame.Rect(screen.get_width() / 2 - 50, screen.get_height() / 2 - 50, 100, 100)
        pygame.draw.rect(screen, "red", button_rect)
        pygame.display.flip()

        # Bouton de la première amélioration (un autoclic)
        if not(hasFirstUp):
            buttonFirstUp = pygame.Rect(screen.get_width() / 4 - 10, screen.get_height() / 2 - 10, 20, 20)
            pygame.draw.rect(screen, "blue", buttonFirstUp)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Incrémente lors d'un clic sur le bouton
                if (button_rect.left < pygame.mouse.get_pos()[0] < button_rect.right
                        and button_rect.top < pygame.mouse.get_pos()[1] < button_rect.bottom):
                    nb_click += 1
                elif (not(hasFirstUp)
                      and screen.get_width() / 4 - 10 < pygame.mouse.get_pos()[0] < screen.get_width() / 4 + 10
                      and screen.get_height() / 2 - 10 < pygame.mouse.get_pos()[1] < screen.get_height() / 2 + 10):
                    hasFirstUp = True
                    firstUpTime = t

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        pygame.display.update()

if __name__ == '__main__':
    main()
