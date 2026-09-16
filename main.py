import math

import pygame
from UI import UI
from message import Message
from events import GAME_END
from events import WINDOW_BREAK

from src.modele.etat import Etat

def main():
    # Démarre le module
    pygame.init()

    ui = UI()

    message = Message(ui.screen, ui.message_font)
    # Message affiché au démarrage
    message.show("MESSAGE D’URGENCE\n"
                 "Vous êtes notre seul espoir.\n"
                 "Une éclipse aura lieu dans 10 minutes. Si elle se produit, ce sera la fin du monde.\n"
                 "Votre mission est simple : remplir entièrement le réservoir de la fusée afin de la lancer et de détruire la Lune avant le debut de l’éclipse.\n"
                 "Chaque seconde compte. Chaque clic peut faire la différence.\n"
                 "Ne nous décevez pas.\n", "Ok")

    running = True

    clock = pygame.time.Clock()
    dt: int = 0
    t: int = 0

    etat: Etat = Etat()

    moon_angle = -math.pi / 2
    button_clicking = False

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Fin réservoir plein
        if etat.score >= 1000000000000000:
            pygame.event.post(pygame.event.Event(GAME_END))

        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001
        else:
            # Fin timer
            pygame.event.post(pygame.event.Event(GAME_END))

        # Affiche la progress bar
        ui.display_progress_bar(etat.score, 100)

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(etat.score)

        if etat.nb_ameliorations > 0 and (t - etat.autocliqueur.temps_premier) / 1000 >= etat.autocliqueur.nb_tot_clics:
            etat.clic_auto()

        if pygame.mouse.get_pressed()[0]:
            # Clic bouton fuëlle
            if ui.check_mouse_position_fuelle_button():
                ui.display_fuelle_button_down()
                if not button_clicking:
                    etat.clic()
            # Clic bouton auto clicker
            elif ui.check_mouse_position_autoclicker_button():
                etat.add_autocliqueur(t)
                ui.display_autoclicker_button_down()
            # Clic bouton fréquence autoclicliker
            elif ui.check_mouse_position_upgrade_frequency_button():
                ui.display_upgrade_frequency_button_down()
            # Clic bouton puissance autoclicliker
            elif ui.check_mouse_position_upgrade_power_button():
                ui.display_upgrade_power_button_down()
            # Clic bouton puissance clic
            elif ui.check_mouse_position_upgrade_clic_button():
                ui.display_upgrade_clic_button_down()
            button_clicking = True
        else:
            button_clicking = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == WINDOW_BREAK:
                etat.score = -1
                pygame.event.post(GAME_END)

            if event.type == GAME_END:
                ui.show_end_message(etat.score)
                running = False

            if message.active:
                message.handle_event(event)

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        message.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
