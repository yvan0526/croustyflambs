import math

import pygame

def main():
    # Démmarre le module
    pygame.init()
    # définit l'écran et sa taille, retourne la surface pour le dessin
    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)
    # Pour savoir quand la boucle du jeu se termine
    running = True

    # Image de fond
    background_image = pygame.image.load("assets/Background.png")

    # Image écran compteur
    screen_score_image = pygame.image.load("assets/Screen_Score.png")

    # Images bouton
    button_up_image = pygame.image.load("assets/Button_Up.png")
    button_down_image = pygame.image.load("assets/Button_Down.png")

    # Police d'écriture nb_click
    font = pygame.font.Font("assets/EarlyGameBoy.ttf", 16)
    score = 100

    # Bouton
    button_rect = pygame.Rect(296, 220, 48, 48)

    # Affichage initial
    screen.blit(background_image, (0, 0))
    screen.blit(button_up_image, (296, 220))

    # Boucle de l'animation
    while running:
        # Texte score
        screen.blit(screen_score_image, (282, 185))
        score_text = font.render(f"{score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (319, 194)
        screen.blit(score_text, score_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Incrémente lors d'un clic sur le bouton
                if (button_rect.left < pygame.mouse.get_pos()[0] < button_rect.right
                        and button_rect.top < pygame.mouse.get_pos()[1] < button_rect.bottom):
                    score += 1
                    screen.blit(button_down_image, (296, 220))
            elif event.type == pygame.MOUSEBUTTONUP:
                screen.blit(button_up_image, (296, 220))

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        pygame.display.update()

if __name__ == '__main__':
    main()
