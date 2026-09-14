import pygame

def main():
    # Démmarre le module
    pygame.init()
    # définit l'écran et sa taille, retourne la surface pour le dessin
    screen = pygame.display.set_mode((1280, 720))
    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True

    font = pygame.font.SysFont(None, 80)

    # Boucle de l'animation
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text = font.render('Croustyflambs', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = ((int)(screen.get_width() / 2), (int)(screen.get_height() / 2))

        screen.fill((200, 255, 200))
        screen.blit(text, text_rect)

        pygame.display.update()

if __name__ == '__main__':
    main()
