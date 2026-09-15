import pygame

class Message():
    """ Affichage d'un message au centre de l'écran """

    def __init__(self, screen):
        # Crée un objet avec la font par défaut
        self.font = pygame.font.Font("assets/EarlyGameBoy.ttf", 16)
        # Conserve la surface où afficher
        self.screen = screen

    def print(self, message):
        """ Affiche le message au centre """
        # Calcule l'image à afficher
        image = self.font.render(f'{message}', True, "black")
        # La position où l'afficher
        rect = image.get_rect()
        # Force la position au centre de l'écran
        rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        # Finalement affiche le message sur la surface
        self.screen.blit(image, rect)
