import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font


class UI:
    # Écran pour l'affichage
    screen: Surface

    # Image de fond
    background_image: Surface

    # Image écran compteur
    screen_score_image: Surface

    # Images bouton
    button_up_image: Surface
    button_down_image: Surface

    # Police d'écriture score
    score_font: Font

    # Bouton
    button_rect: Rect

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)

        # Image de fond
        self.background_image = pygame.image.load("assets/Background.png")

        # Image écran compteur
        self.screen_score_image = pygame.image.load("assets/Screen_Score.png")

        # Images bouton
        self.button_up_image = pygame.image.load("assets/Button_Up.png")
        self.button_down_image = pygame.image.load("assets/Button_Down.png")

        # Police d'écriture nb_click
        self.score_font = pygame.font.Font("assets/EarlyGameBoy.ttf", 16)

        # Bouton
        self.button_rect = pygame.Rect(296, 220, 48, 48)

        # Affichage initial
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.button_up_image, (296, 220))

    def display_score(self, score: int):
        self.screen.blit(self.screen_score_image, (282, 185))
        score_text = self.score_font.render(f"{score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (319, 194)
        self.screen.blit(score_text, score_text_rect)

    def check_mouse_click_fuelle_button(self):
        return (self.button_rect.left < pygame.mouse.get_pos()[0] < self.button_rect.right
                        and self.button_rect.top < pygame.mouse.get_pos()[1] < self.button_rect.bottom)

    def display_button_down(self):
        self.screen.blit(self.button_down_image, (296, 220))

    def display_button_up(self):
        self.screen.blit(self.button_up_image, (296, 220))