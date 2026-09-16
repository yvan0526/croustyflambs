import math

import pygame
from pygame import Surface
from pygame.ftfont import Font

from message import Message


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
    # Image bouton téléphone (stagiaire)
    phone_button_image: Surface
    # Image micro
    micro_1_image = Surface
    micro_2_image = Surface
    micro_3_image = Surface
    micro_4_image = Surface
    micro_5_image = Surface
    micro_6_image = Surface
    micro_7_image = Surface
    micro_8_image = Surface
    micro_9_image = Surface
    micro_10_image = Surface
    micro_11_image = Surface
    micro_12_image = Surface

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
        #Police d'écriture message
        self.message_font = pygame.font.Font("assets/PressStart2P.ttf", 8)
        # Progress bar
        self.progress_bar_background_image = pygame.image.load("assets/Bar_Background.png")
        self.progress_bar_image = pygame.image.load("assets/Bar.png")
        # Bouton upgrade clic
        self.upgrade_clic_button_image = pygame.image.load("assets/Button_Upgrade_Down.png")
        # Bouton auto clicker
        self.autoclicker_button_image = pygame.image.load("assets/Button_AutoClicker_Down.png")
        # Bouton upgrade power
        self.upgrade_power_button_image = pygame.image.load("assets/Button_UpgradePower_Down.png")
        # Bouton upgrade frequecy
        self.upgrade_frequency_button_image = pygame.image.load("assets/Button_UpgradeFreq_Down.png")
        # Bouton téléphone (stagiaire)
        self.phone_button_image = pygame.image.load("assets/Button_Stagiaire_Down.png")
        # Trappe micro
        self.micro_1_image = pygame.image.load("assets/Micro/Micro_1.png")
        self.micro_2_image = pygame.image.load("assets/Micro/Micro_2.png")
        self.micro_3_image = pygame.image.load("assets/Micro/Micro_3.png")
        self.micro_4_image = pygame.image.load("assets/Micro/Micro_4.png")
        self.micro_5_image = pygame.image.load("assets/Micro/Micro_5.png")
        self.micro_6_image = pygame.image.load("assets/Micro/Micro_6.png")
        self.micro_7_image = pygame.image.load("assets/Micro/Micro_7.png")
        self.micro_8_image = pygame.image.load("assets/Micro/Micro_8.png")
        self.micro_9_image = pygame.image.load("assets/Micro/Micro_9.png")
        self.micro_10_image = pygame.image.load("assets/Micro/Micro_10.png")
        self.micro_11_image = pygame.image.load("assets/Micro/Micro_11.png")
        self.micro_12_image = pygame.image.load("assets/Micro/Micro_12.png")

        # Liste micro
        self.micro_images = [
            self.micro_1_image, self.micro_2_image, self.micro_3_image,
            self.micro_4_image, self.micro_5_image, self.micro_6_image,
            self.micro_7_image, self.micro_8_image, self.micro_9_image,
            self.micro_10_image, self.micro_11_image, self.micro_12_image,
        ]

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
        return 296 < pygame.mouse.get_pos()[0] < 344 and 220 < pygame.mouse.get_pos()[1] < 268

    def check_mouse_position_phone_button(self):
        return 74 < pygame.mouse.get_pos()[0] < 87 and 254 < pygame.mouse.get_pos()[1] < 267

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

    def display_phone_button_down(self):
        self.screen.blit(self.phone_button_image, (74,254))

    def display_micro(self, frame_index: int):
        frame_index = max(0, min(frame_index, len(self.micro_images) - 1))
        self.screen.blit(self.micro_images[frame_index], (40, 175))

    def show_end_message(self, score):
        message_end = Message(self.screen, self.message_font)
        message_credits = Message(self.screen, self.message_font)
        if score < 0:  # Casser la fenêtre met le score à une valeur négative et termine le jeu
            message_end.show("Patron : Mais que faites-vous?! Je ne vous paie pas pour cela !", "Suivant")
            message_end.show("Patron : Vous êtes renvoyé·e !", "Suivant")
            message_end.show("VOUS AVEZ ÉTÉ RENVOYÉ·E. TOUT LE MONDE EST MORT.", "Fin")
        elif score < 1:
            message_end.show("VOTRE FUSÉE N'A PAS DÉCOLLÉ.\
                            LA FACE CACHÉE DE LA LUNE S'EST RÉVELÉE. TOUT LE MONDE EST MORT.", "Fin")
        elif score < 410000000000000:
            message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE S'EST MALHEUREUSEMENT ÉCRASÉE PAR MANQUE DE CARBURANT.\
                            L'IUT2 DE GRENOBLE A ÉTÉ RASÉ.\
                            CÉDRIC GÉROT, S'ÉTANT RECONVERTI, A ÉTÉ ÉLU PRÉSIDENT DE LA RÉPUBLIQUE FRANÇAISE AVEC 69% DES VOIX.",
                             "Fin")
        elif score < 430000000000000:
            message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE, S'EST ARRÊTÉE, ET SE PERD DANS L'ESPACE.\
                            L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ.", "Fin")
        elif score < 750000000000000:
            message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE ET S'EST ARRÊTÉE EN ORBITE LUNAIRE.\
                            DES HABITANTS DE LA LUNE ONT FAIT REPARTIR LA FUSÉE VERS LA TERRE.\
                            LA POPULATION TERRESTRE EST RÉDUITE EN ESCLAVAGE.", "Fin")
        elif score <= 999999999999999:
            message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A LÉGÈREMENT DÉVIÉ DE SA TRAJECTOIRE ET SE DIRIGE VERS LE SOLEIL.\
                            LE SOLEIL EXPLOSE.\
                            8 MINUTES PLUS TARD, TOUT LE MONDE EST MORT.", "Fin")
        elif score >= 1000000000000000:
            message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A ATTEINT SA CIBLE. LA LUNE EXPLOSE.\
                            LES DÉBRIS DE LA LUNE RETOMBENT SUR LA TERRE.\
                            TOUT LE MONDE EST MORT.", "Fin")
        else:
            message_end.show("undefined Fin", "Undefined")
        message_credits.show("Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\
                                                        Création : équipe des croustiflambs (le b est muet)\
                                                        Programmation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\
                                                        Assets graphiques : Emma DHOURY\
                                                        Sons : Emma DHOURY\
                                                        Remerciements :\
                                                        Merci à Jean-Pierre CHEVALLET pour son cours sur le langage Python et ses conseils lors du développement.\
                                                        Merci à l'équipe enseignante du BUT Informatique de l'université Grenoble-Alpes.\
                                                        Enfin, merci à vous d'avoir joué !", "Quitter")