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
    # Image diode
    diode_image: Surface
    # Image LED
    led_image: Surface

    # Police d'écriture score
    score_font: Font
    # Police d'écriture message
    message_font: Font
    # Police d'écriture prix
    price_font: Font
    # Police d'écriture écran upgrade
    upgrade_screen_font: Font

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
        # Police d'écriture message
        self.message_font = pygame.font.Font("assets/PressStart2P.ttf", 8)
        # Police d'écriture prix
        self.price_font = pygame.font.Font("assets/QuinqueFive.ttf", 5)
        # Police d'écriture écrans upgrades
        self.upgrade_screen_font = pygame.font.Font("assets/QuinqueFive.ttf", 5)
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
        # Diode
        self.diode_image = pygame.image.load("assets/Diode_On.png")
        # LED
        self.led_image = pygame.image.load("assets/Led_On.png")

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

    def messagestart(self):
        message = Message(self.screen, self.message_font)
        # Message affiché au démarrage
        message.show("MESSAGE D’URGENCE\n"
                     "Vous êtes notre seul espoir.\n"
                     "Une éclipse aura lieu dans 10 minutes. Si elle se produit, ce sera la fin du monde.\n"
                     "Votre mission est simple : remplir entièrement le réservoir de la fusée afin de la lancer et de détruire la Lune avant le debut de l’éclipse.\n"
                     "Chaque seconde compte. Chaque clic peut faire la différence.\n"
                     "Ne nous décevez pas.\n", "Ok")

    def display_progress_bar(self, score, score_max):
        self.screen.blit(self.progress_bar_background_image, (200, 332))
        x = min(-40 + (score / score_max) * 240, 200)
        self.screen.blit(self.progress_bar_image, (x, 332))

    def check_mouse_position_upgrade_clic_button(self):
        return 449 < pygame.mouse.get_pos()[0] < 482 and 190 < pygame.mouse.get_pos()[1] < 211

    def display_upgrade_clic_button_down(self):
        self.screen.blit(self.upgrade_clic_button_image, (449, 190))

    def display_led_upgrade_clic(self):
        self.screen.blit(self.led_image, (486, 192))

    def check_mouse_position_autoclicker_button(self):
        return 552 < pygame.mouse.get_pos()[0] < 585 and 190 < pygame.mouse.get_pos()[1] < 211

    def display_autoclicker_button_down(self):
        self.screen.blit(self.autoclicker_button_image, (552, 190))

    def display_led_upgrade_autoclicker(self):
        self.screen.blit(self.led_image, (589, 192))

    def check_mouse_position_upgrade_power_button(self):
        return 552 < pygame.mouse.get_pos()[0] < 585 and 229 < pygame.mouse.get_pos()[1] < 250

    def display_upgrade_power_button_down(self):
        self.screen.blit(self.upgrade_power_button_image, (552, 229))

    def display_led_upgrade_power(self):
        self.screen.blit(self.led_image, (589, 231))

    def check_mouse_position_upgrade_frequency_button(self):
        return 552 < pygame.mouse.get_pos()[0] < 585 and 252 < pygame.mouse.get_pos()[1] < 273

    def display_upgrade_frequency_button_down(self):
        self.screen.blit(self.upgrade_frequency_button_image, (552, 252))

    def display_led_upgrade_frequency(self):
        self.screen.blit(self.led_image, (589, 254))

    def display_diodes(self, nb_diodes):
        for i in range(min(nb_diodes, 10)):
            self.screen.blit(self.diode_image, (513 + (i * 9), 215))

    def display_clic_price(self, price):
        price_text = self.price_font.render(f"{price}", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (428, 201)
        self.screen.blit(price_text, price_text_rect)

    def display_autoclicker_price(self, price):
        price_text = self.price_font.render(f"{price}", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (531, 201)
        self.screen.blit(price_text, price_text_rect)

    def display_power_price(self, price):
        price_text = self.price_font.render(f"{price}", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (531, 240)
        self.screen.blit(price_text, price_text_rect)

    def display_frequency_price(self, price):
        price_text = self.price_font.render(f"{price}", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (531, 263)
        self.screen.blit(price_text, price_text_rect)

    def display_clic_power(self, clic_power):
        clic_power_text = self.upgrade_screen_font.render(f"{clic_power}f/c", True, (255, 255, 255))
        clic_power_text_rect = clic_power_text.get_rect()
        clic_power_text_rect.center = (454, 229)
        self.screen.blit(clic_power_text, clic_power_text_rect)

    def display_fuelle_per_second(self, nb_autoclicker, autoclicker_power, autoclicker_frequency):
        clic_power_text = self.upgrade_screen_font.render(f"{nb_autoclicker * autoclicker_power * autoclicker_frequency}f/s", True, (255, 255, 255))
        clic_power_text_rect = clic_power_text.get_rect()
        clic_power_text_rect.center = (557, 291)
        self.screen.blit(clic_power_text, clic_power_text_rect)

    def show_end_message(self, score):
        message_end = Message(self.screen, self.message_font)
        message_credits = Message(self.screen, self.message_font)

    def get_message_text(self, score):
        if score < 0:  # Casser la fenêtre met le score à une valeur négative et termine le jeu
            return "Patron : Mais que faites-vous?! Je ne vous paie pas pour cela !\nPatron : Vous êtes renvoyé·e !\n\nVous avez été renvoyé·e. Tout le monde est mort."
        elif score < 1:
            return "Votre fusée n'a pas décollé.\nLa face cachée de la Lune s'est révélée. Tout le monde est mort."
        elif score < 410000000000000:
            return "Votre fuse a décollé. Elle s'est malheureusement écrasée par manque de carburant.\nL'IUT2 de Grenoble a été rasé.\nCédric Gérot, s'étant reconverti, a été élu président de la République Française avec 69% des voix."
        elif score < 430000000000000:
            return "Votre fusée a décollé. Elle a dévié de sa trajectoire, s'est arrêtée, et se perd dans l'espace.\nL'éclipse a eu lieu. Rien n'est arrivé. Le monde est sauvé."
        elif score < 750000000000000:
            return "Votre fusée a décollé. Elle a dévié de sa trajectoire et s'est arrêtée en orbite lunaire.\nDes habitants de la Lune ont fait repartir la fusée vers la Terre.\nLa population terrestre est réduit en esclavage."
        elif score <= 999999999999999:
            return "Votre fusée a décollé. Elle a légèrement dévié de sa trajectoire et se dirige vers le Soleil.\nUne semaine plus tard, le Soleil explose.\n8 minutes plus tard, tout le monde est mort."
        elif score >= 1000000000000000:
            return "Votre fusée a décollé. Elle a atteint sa cible. La Lune explose.\nLes débris de la Lune retombent sur la Terre.\nTout le monde est mort."
        else:
            return "undefined Fin"

    def get_credits_text(self):
        return "Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\nCréation : équipe des croustiflambs (le b est muet)\nProgrammation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\nSons : Emma DHOURY\nAssets graphiques : Emma DHOURY\nDessin original de la fusée : Hergé, Bob DE MOOR (Objectif Lune, 1953, éditions Casterman)\nRemerciements :\nMerci à Jean-Pierre CHEVALLET pour son cours sur le langage Python et ses conseils lors du développement.\nMerci à l'équipe enseignante du BUT Informatique de l'université Grenoble-Alpes.\nEnfin, merci à vous d'avoir joué !"
