import math

from UI import UI
from message import Message
from events import *

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
    # millisecondes * secondes * minutes
    timer_end = 1000 * 60 * 1

    etat: Etat = Etat()

    moon_start_angle = -math.pi / 2
    moon_angle = moon_start_angle
    button_clicking = False

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Fin réservoir plein
        if etat.score >= 1000000000000000:
            etat.score = 1000000000000000
            running = False

        for event in pygame.event.get():
            if message.active:
                message.handle_event(event)

            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == WINDOW_BREAK:
                etat.score = -1
                pygame.event.post(pygame.event.Event(GAME_END))

            elif event.type == GAME_END:
                message.show(ui.get_message_text(etat.score), 'Fin')
                pygame.event.post(pygame.event.Event(CREDITS))

            elif event.type == CREDITS:
                message.show(ui.get_credits_text(), 'Quitter')
                pygame.event.post(pygame.event.Event(pygame.QUIT))


        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            angle = abs(moon_start_angle) / timer_end * dt
            moon_angle += angle
        else:
            # Fin timer
            print("fin timer")
            running = False
            pygame.event.post(pygame.event.Event(GAME_END))

        # Affiche la progress bar
        ui.display_progress_bar(etat.score, 100)

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(etat.score)

        # LEDs
        if etat.peut_add_valeur_clic():
            ui.display_led_upgrade_clic()
        if etat.peut_add_autocliqueur():
            ui.display_led_upgrade_autoclicker()
        if etat.peut_add_autoclic_val():
            ui.display_led_upgrade_power()
        if etat.peut_add_autoclic_cps():
            ui.display_led_upgrade_frequency()

        # Diodes
        ui.display_diodes(etat.autocliqueur.quantite)

        # Prix
        ui.display_clic_price(etat.PRIX_AMELIORATION[etat.valeur_clic])
        ui.display_autoclicker_price(etat.PRIX_AMELIORATION[etat.autocliqueur.quantite])
        ui.display_power_price(etat.PRIX_AMELIORATION[etat.autocliqueur.valeur])
        ui.display_frequency_price(etat.PRIX_AMELIORATION[etat.autocliqueur.cps])

        # Valeur du clic screen
        ui.display_clic_power(etat.valeur_clic)

        # Fuëlle par seconde screen
        ui.display_fuelle_per_second(etat.autocliqueur.quantite, etat.autocliqueur.valeur, etat.autocliqueur.cps)

        if (t - etat.autocliqueur.temps_premier) * etat.autocliqueur.cps / 1000 >= etat.autocliqueur.nb_tot_clics:
            etat.clic_auto()

        # Gestion de la souris
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
                etat.add_autoclic_cps()
                ui.display_upgrade_frequency_button_down()
            # Clic bouton puissance autoclicliker
            elif ui.check_mouse_position_upgrade_power_button():
                etat.add_autoclic_val()
                ui.display_upgrade_power_button_down()
            # Clic bouton puissance clic
            elif ui.check_mouse_position_upgrade_clic_button():
                etat.add_valeur_clic()
                ui.display_upgrade_clic_button_down()
            button_clicking = True
        else:
            button_clicking = False

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        message.draw()
        pygame.display.update()

    game_quit = False
    while not game_quit:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game_quit = True
        else:
            message.show(ui.get_message_text(etat.score), 'Fin')
            while message.active:
                message.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if message.active:
                        message.handle_event(event)
            message.show(ui.get_credits_text(), 'Quitter')
            while message.active:
                message.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    message.handle_event(event)
            game_quit = True

if __name__ == '__main__':
    main()
