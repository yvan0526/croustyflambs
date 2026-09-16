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
    sky_images: list
    moon_images: list
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
    # Image bouton téléphone (stagiaire)
    micro_button_image: Surface
    # Images micro
    micro_images: list
    # Fin 100
    end_100_images: list
    # Fin joyeuse
    end_happy_images: list
    # Fin IUT
    end_iut_images: list
    # Fin luniens
    end_luniens_images: list
    # Fin soleil
    end_sun_images: list
    # Fin Blanchon
    end_blanchon_images: list

    # Police d'écriture score
    score_font: Font
    # Police d'écriture message
    message_font: Font
    # Police d'écriture prix
    price_font: Font
    # Police d'écriture écran upgrade
    upgrade_screen_font: Font

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)

        # Bureau
        self.background_image = pygame.image.load("assets/Background.png")

        # Fenêtre
        self.sky_images = []
        self.moon_images = []
        for i in range(5):
            self.sky_images.append(pygame.image.load(f"assets/Sky_{i + 1}.png"))
            self.moon_images.append(pygame.image.load(f"assets/Moon_{i + 1}.png"))

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
        # Bouton téléphone (stagiaire)
        self.micro_button_image = pygame.image.load("assets/Button_Stagiaire.png")
        # Liste micro
        self.micro_images = []
        for i in range(12):
            self.micro_images.append(pygame.image.load(f"assets/Micro/Micro_{i + 1}.png"))
        # Fin 100
        self.end_100_images = []
        for i in range(35):
            self.end_100_images.append(pygame.image.load(f"assets/End_100/End_100_{i + 1}.png"))
        # Fin joyeuse
        self.end_happy_images = []
        for i in range(22):
            self.end_happy_images.append(pygame.image.load(f"assets/End_Happy/End_Happy_{i + 1}.png"))
        # Fin IUT
        self.end_iut_images = []
        for i in range(38):
            self.end_iut_images.append(pygame.image.load(f"assets/End_IUT/End_IUT_{i + 1}.png"))
        # Fin luniens
        self.end_luniens_images = []
        for i in range(49):
            self.end_luniens_images.append(pygame.image.load(f"assets/End_Luniens/End_Luniens_{i + 1}.png"))
        # Fin soleil
        self.end_sun_images = []
        for i in range(18):
            self.end_sun_images.append(pygame.image.load(f"assets/End_SunBoom/End_SunBoom_{i + 1}.png"))
        # Fin Blanchon
        self.end_blanchon_images = []
        for i in range(14):
            self.end_blanchon_images.append(pygame.image.load(f"assets/Blanchoon/Blanchoon_{i + 1}.png"))

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
        sun_x = 364
        sun_y = 84
        x1 = sun_x - 319
        y1 = sun_y - 194
        x2 = x1 * math.cos(angle) - y1 * math.sin(angle)
        y2 = x1 * math.sin(angle) + y1 * math.cos(angle)
        x = x2 + 319
        y = y2 + 194

        i = 0
        if 32 <= sun_x - x > 23:
            i = 1
        elif sun_x - x > 14:
            i = 2
        elif sun_x - x > 7:
            i = 3
        else:
            i = 4

        self.screen.blit(self.sky_images[i], (220, 20))
        self.screen.blit(self.moon_images[i], (x, y))

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
        price_text = self.price_font.render(f"{price}F", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (428, 201)
        self.screen.blit(price_text, price_text_rect)

    def display_autoclicker_price(self, price):
        price_text = self.price_font.render(f"{price}F", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (531, 201)
        self.screen.blit(price_text, price_text_rect)

    def display_power_price(self, price):
        price_text = self.price_font.render(f"{price}F", True, (255, 255, 255))
        price_text_rect = price_text.get_rect()
        price_text_rect.center = (531, 240)
        self.screen.blit(price_text, price_text_rect)

    def display_frequency_price(self, price):
        price_text = self.price_font.render(f"{price}F", True, (255, 255, 255))
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
    def display_phone_button_down(self):
        self.screen.blit(self.micro_button_image, (74,254))

    def display_micro(self, frame_index: int):
        frame_index = max(0, min(frame_index, len(self.micro_images) - 1))
        self.screen.blit(self.micro_images[frame_index], (40, 175))

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
        elif score <= 1050000000000000:
            return "Votre fusée a décollé. Elle a atteint sa cible. La Lune explose.\nLes débris de la Lune retombent sur la Terre.\nTout le monde est mort."
        elif score > 1050000000000000:
            return "Votre fusée a décollé. Elle a légèrement dévié de sa trajectoire et se dirige vers le Soleil.\nUne semaine plus tard, le Soleil explose.\n8 minutes plus tard, tout le monde est mort."
        else:
            return "undefined Fin"

    def get_credits_text(self):
        return "Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\nCréation : équipe des croustiflambs (le b est muet)\nProgrammation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\nSons : Emma DHOURY\nAssets graphiques : Emma DHOURY\nDessin original de la fusée : Hergé, Bob DE MOOR (Objectif Lune, 1953, éditions Casterman)\nRemerciements :\nMerci à Jean-Pierre CHEVALLET pour son cours sur le langage Python et ses conseils lors du développement.\nMerci à l'équipe enseignante du BUT Informatique de l'université Grenoble-Alpes.\nEnfin, merci à vous d'avoir joué !"
