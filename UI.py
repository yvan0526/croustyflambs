import math

import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font


class UI:
    # Écran pour l'affichage
    screen: Surface
    # Image du bureau
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
    # Images bouton fuelle
    fuelle_button_image: Surface
    # Images progress bar
    progress_bar_background_image: Surface
    progress_bar_image: Surface
    # Image bouton upgrade clic
    upgrade_clic_button_image: Surface
    # Image bouton auto clicker
    autoclicker_button_image: Surface
    # Image bouton upgrade power
    upgrade_power_button_image: Surface
    # Image bouton upgrade frequecy
    upgrade_frequency_button_image: Surface

    # Police d'écriture score
    score_font: Font

    # Position de la lune
    sun_x: int
    sun_y: int

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)

        # Bureau
        self.background_image = pygame.image.load("assets/Background.png")
        # Fenêtre
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
        # Bouton fuelle
        self.fuelle_button_image = pygame.image.load("assets/Button_Down.png")
        # Police d'écriture score
        self.score_font = pygame.font.Font("assets/PressStart2P.ttf", 16)
        # Progress bar
        self.progress_bar_background_image = pygame.image.load("assets/Bar_Background.png")
        self.progress_bar_image = pygame.image.load("assets/Bar.png")
        # Bouton upgrade clic
        upgrade_clic_button_image = pygame.image.load("assets/Button_Upgrade_Down.png")
        # Bouton auto clicker
        autoclicker_button_image = pygame.image.load("assets/Button_AutoClicker_Down.png")
        # Bouton upgrade power
        upgrade_power_button_image = pygame.image.load("assets/Button_UpgradePower_Down.png")
        # Bouton upgrade frequecy
        upgrade_frequency_button_image = pygame.image.load("assets/Button_UpgradeFreq_Down.png")

    def display_background(self):
        self.screen.blit(self.background_image, (0, 0))

    def display_score(self, score: int):
        if score >= 1000000000000000:
            score_text = self.score_font.render(f"{score // 1000000000000000}P", True, (255, 255, 255))
        elif score >= 1000000000000:
            score_text = self.score_font.render(f"{score // 1000000000000}T", True, (255, 255, 255))
        elif score >= 1000000000:
            score_text = self.score_font.render(f"{score//1000000000}G", True, (255, 255, 255))
        elif score >= 1000000:
            score_text = self.score_font.render(f"{score // 1000000}M", True, (255, 255, 255))
        elif score >= 1000:
            score_text = self.score_font.render(f"{score//1000}K", True, (255, 255, 255))
        else:
            score_text = self.score_font.render(f"{score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (320, 196)
        self.screen.blit(score_text, score_text_rect)

    def check_mouse_position_fuelle_button(self):
        return 296 < pygame.mouse.get_pos()[0] < 336 and 220 < pygame.mouse.get_pos()[1] < 260

    def display_fuelle_button_down(self):
        self.screen.blit(self.fuelle_button_image, (296, 220))

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

    def display_progress_bar(self, score, score_max):
        self.screen.blit(self.progress_bar_background_image, (200, 332))
        x = min(-40 + (score / score_max) * 240, 200)
        self.screen.blit(self.progress_bar_image, (x, 332))

    def display_upgrade_clic_button_down(self):
        self.screen.blit(self.upgrade_clic_button_image, (448, 190))

    def display_autoclicker_button_down(self):
        self.screen.blit(self.autoclicker_button_image, (552, 190))

    def display_upgrade_power_button_down(self):
        self.screen.blit(self.upgrade_power_button_image, (552, 229))

    def display_upgrade_frequency_button_down(self):
        self.screen.blit(self.upgrade_frequency_button_image, (552, 252))
