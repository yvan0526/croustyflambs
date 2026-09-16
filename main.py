import math

import pygame

import animations
from UI import UI
from animation import Animation
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
    timer_end = 1000 * 60 * 10

    etat: Etat = Etat()

    moon_start_angle = -math.pi / 2
    moon_angle = moon_start_angle
    button_clicking = False

    #Stagiaire
    stagiaire_apparition = timer_end /2
    stagiaire_message = False
    stagiaire_message_ferme = False
    micro_animation = 0
    micro_animation_lance = False
    micro_ouverture_terminee = False
    micro_fermeture_lancee = False
    micro_fermeture_debut = 0
    micro_frame_duration = 100 #ms par frame d'animation
    message_actif_precedent = False

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Message stagiaire
        if t >= stagiaire_apparition and not stagiaire_message:
            message.show("On a envoyé un stagiaire pour vous aider !", "Ok")
            stagiaire_message = True
            stagiaire_message_ferme = True

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

            # Clic sur le bouton téléphone
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                    and micro_animation_lance and not micro_fermeture_lancee
                    and ui.check_mouse_position_phone_button()):
                if etat.peut_appeler_stagiaire():
                    etat.appeler_stagiaire(t)
                    if etat.stagiaire_epuise():
                        micro_fermeture_lancee = True
                        micro_fermeture_debut = t

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
        # TODO: Mettre le bon score max
        ui.display_progress_bar(etat.score, 100)

        # Affiche le bureau
        ui.display_background()

        # Affiche la lumière de la barre de progression
        # TODO: Mettre le bon score max
        if 100 <= etat.score < 105:
            ui.display_green_ligth()
        elif etat.score >= 105:
            ui.display_red_ligth()

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
        if etat.peut_debloquer_clic_droit():
            ui.display_led_right_clic()

        # Diodes
        ui.display_diodes(etat.autocliqueur.quantite)

        # Bouton clic droit
        if etat.clic_droit_debloque:
            ui.display_right_clic_button()

        # Prix
        ui.display_clic_price(etat.calc_prix(etat.valeur_clic, "faible"))
        ui.display_autoclicker_price(etat.calc_prix(etat.autocliqueur.quantite, "moyen"))
        ui.display_power_price(etat.calc_prix(etat.autocliqueur.valeur, "faible"))
        ui.display_frequency_price(etat.calc_prix(etat.autocliqueur.cps, "faible"))
        ui.display_right_clic_price(1000)

        # Valeur du clic screen
        ui.display_clic_power(etat.valeur_clic)

        # Fuëlle par seconde screen
        ui.display_fuelle_per_second(etat.autocliqueur.quantite, etat.autocliqueur.valeur, etat.autocliqueur.cps)
            
        # Détecte la fermeture du message stagiaire pour lancer l'animation
        if stagiaire_message_ferme and message_actif_precedent and not message.active:
            micro_animation = t
            micro_animation_lance = True
            stagiaire_message_ferme = False

        message_actif_precedent = message.active

        # Animation micro
        if micro_fermeture_lancee:
            temps_ecoule = t - micro_fermeture_debut
            frame_index = len(ui.micro_images) - 1 - (temps_ecoule // micro_frame_duration)
            if frame_index >= 0:
                ui.display_micro(frame_index)

        elif micro_animation_lance:
            temps_ecoule = t - micro_animation
            frame_index = temps_ecoule // micro_frame_duration

            if frame_index < len(ui.micro_images):
                # Animation d'ouverture en cours
                ui.display_micro(frame_index)
            else:
                # Animation terminée : le micro reste affiché (image 12 = bouton au repos)
                micro_ouverture_terminee = True
                ui.display_micro(len(ui.micro_images) - 1)
                # Clic sur le bouton
                if pygame.mouse.get_pressed()[0] and ui.check_mouse_position_phone_button():
                    ui.display_phone_button_down()

        if micro_ouverture_terminee and not micro_fermeture_lancee:
            ui.display_frequency_stagiaire(etat.appels_stagiaire_restants())


        if (t - etat.autocliqueur.temps_ref) * etat.autocliqueur.cps / 1000 >= etat.autocliqueur.nb_tot_clics:
            etat.clic_auto()

        # Gestion de la souris
        coffee_actif = etat.coffee_actif(t)

        if (pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2] and etat.clic_droit_debloque) and not message.active:
            # Clic bouton fuëlle
            if ui.check_mouse_position_fuelle_button():
                ui.display_fuelle_button_down()
                if not button_clicking or coffee_actif:
                    etat.clic()
            # Clic bouton auto clicker
            elif ui.check_mouse_position_autoclicker_button():
                if not button_clicking:
                    etat.add_autocliqueur(t)
                ui.display_autoclicker_button_down()
            # Clic bouton fréquence autoclicliker
            elif ui.check_mouse_position_upgrade_frequency_button():
                if not button_clicking:
                    etat.add_autoclic_cps(t)
                ui.display_upgrade_frequency_button_down()
            # Clic bouton puissance autoclicliker
            elif ui.check_mouse_position_upgrade_power_button():
                if not button_clicking:
                    etat.add_autoclic_val()
                ui.display_upgrade_power_button_down()
            # Clic bouton puissance clic
            elif ui.check_mouse_position_upgrade_clic_button():
                if not button_clicking:
                    etat.add_valeur_clic()
                ui.display_upgrade_clic_button_down()
            # Clic bouton clic droit
            elif ui.check_mouse_position_right_clic_button():
                if not button_clicking:
                    etat.debloque_clic_droit()
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

    # Ending handler
    game_quit = False
    while not game_quit:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game_quit = True
        else:
            # Animation de fin
            animation_fin = animations.get_end_animation(ui, etat.score)
            while not animation_fin.is_finished:
                dt = clock.tick(60)
                t += dt
                animation_fin.play(t)

            # Message de fin
            message.show(ui.get_message_text(etat.score), 'Fin')
            while message.active:
                message.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if message.active:
                        message.handle_event(event)

            # Crédits
            message.show(ui.get_credits_text(), 'Quitter')
            while message.active:
                message.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    message.handle_event(event)
            game_quit = True

if __name__ == '__main__':
    main()
