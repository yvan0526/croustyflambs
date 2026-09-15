import math

import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font


class UI:
    # Écran pour l'affichage
    screen: Surface

    # Image de fond
    background_image: Surface

    # Images fenêtre
    sky_1_image: Surface
    sky_2_image: Surface
    sky_3_image: Surface
    sky_4_image: Surface
    sky_5_image: Surface
    moon_1_image: Surface
    moon_2_image: Surface
    moon_3_image: Surface
    moon_4_image: Surface
    moon_5_image: Surface

    # Image écran compteur
    screen_score_image: Surface

    # Images bouton
    button_up_image: Surface
    button_down_image: Surface

    # Police d'écriture score
    score_font: Font

    # Bouton
    button_rect: Rect

    # Position de la lune
    sun_x: int
    sun_y: int

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)

        # Image de fond
        self.background_image = pygame.image.load("assets/Background.png")

        # Images fenêtre
        self.sky_1_image = pygame.image.load("assets/Sky_1.png")
        self.sky_2_image = pygame.image.load("assets/Sky_2.png")
        self.sky_3_image = pygame.image.load("assets/Sky_3.png")
        self.sky_4_image = pygame.image.load("assets/Sky_4.png")
        self.sky_5_image = pygame.image.load("assets/Sky_5.png")

        self.moon_1_image = pygame.image.load("assets/Moon_1.png")
        self.moon_2_image = pygame.image.load("assets/Moon_2.png")
        self.moon_3_image = pygame.image.load("assets/Moon_3.png")
        self.moon_4_image = pygame.image.load("assets/Moon_4.png")
        self.moon_5_image = pygame.image.load("assets/Moon_5.png")

        self.sun_x = 364
        self.sun_y = 84

        # Image écran compteur
        self.screen_score_image = pygame.image.load("assets/Screen_Score.png")

        # Images bouton
        self.button_up_image = pygame.image.load("assets/Button_Up.png")
        self.button_down_image = pygame.image.load("assets/Button_Down.png")

        # Police d'écriture score
        self.score_font = pygame.font.Font("assets/EarlyGameBoy.ttf", 16)

        # Bouton
        self.button_rect = pygame.Rect(296, 220, 48, 48)

    def display_init(self):
        self.display_background()
        self.display_button_up()

    def display_background(self):
        self.screen.blit(self.background_image, (0, 0))

    def display_score(self, score: int):
        self.screen.blit(self.screen_score_image, (282, 185))
        score_text = self.score_font.render(f"{score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (319, 194)
        self.screen.blit(score_text, score_text_rect)

    def check_mouse_position_fuelle_button(self):
        return (self.button_rect.left < pygame.mouse.get_pos()[0] < self.button_rect.right
                        and self.button_rect.top < pygame.mouse.get_pos()[1] < self.button_rect.bottom)

    def display_button_down(self):
        self.screen.blit(self.button_down_image, (296, 220))

    def display_button_up(self):
        self.screen.blit(self.button_up_image, (296, 220))

    def display_window(self, angle):
        x1 = self.sun_x - 319
        y1 = self.sun_y - 194

        x2 = x1 * math.cos(angle) - y1 * math.sin(angle)
        y2 = x1 * math.sin(angle) + y1 * math.cos(angle)

        x = x2 + 319
        y = y2 + 194

        if self.sun_x - x > 32:
            self.screen.blit(self.sky_1_image, (220, 20))
            self.screen.blit(self.moon_1_image, (x, y))
        elif self.sun_x - x > 23:
            self.screen.blit(self.sky_2_image, (220, 20))
            self.screen.blit(self.moon_2_image, (x, y))
        elif self.sun_x - x > 14:
            self.screen.blit(self.sky_3_image, (220, 20))
            self.screen.blit(self.moon_3_image, (x, y))
        elif self.sun_x - x > 7:
            self.screen.blit(self.sky_4_image, (220, 20))
            self.screen.blit(self.moon_4_image, (x, y))
        else:
            self.screen.blit(self.sky_5_image, (220, 20))
            self.screen.blit(self.moon_5_image, (x, y))
