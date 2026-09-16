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

    hasFirstUp: bool = False
    etat: Etat = Etat()

    moon_angle = -math.pi / 2
    button_clicking = False


    #Stagiaire
    stagiaire_cost = [1000000 * (2 ** i) for i in range(10)]  # 10 paliers, jusqu'à 512M
    stagiaire_apparition = 5 * 60 * 1000  # 5 minutes en millisecondes
    stagiaire_disponible = False
    stagiaire_message = False
    coffee_duration = 10000  # 10 secondes en millisecondes

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Message stagiaire
        if t >= stagiaire_apparition and not stagiaire_message:
            message.show("On a envoyé un stagiaire pour vous aider !", "Ok")
            stagiaire_disponible = True
            stagiaire_message = True

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

        # TODO: Refaire ça proprement
        if not (hasFirstUp):
            buttonFirstUp = pygame.Rect(ui.screen.get_width() / 4 - 10, ui.screen.get_height() / 2 - 10, 20, 20)
            pygame.draw.rect(ui.screen, "blue", buttonFirstUp)
        elif (t - etat.autocliqueur.temps_premier) / 1000 >= etat.autocliqueur.nb_tot_clics:
            etat.clic_auto()
            etat.autocliqueur.nb_tot_clics += 1

        if pygame.mouse.get_pressed()[0]:
            # Clic bouton fuëlle
            if ui.check_mouse_position_fuelle_button():
                ui.display_fuelle_button_down()
                if not button_clicking:
                    etat.clic()
            # Clic bouton auto clicker
            elif (not (hasFirstUp) and etat.score >= 20
                  and ui.screen.get_width() / 4 - 10 < pygame.mouse.get_pos()[0] < ui.screen.get_width() / 4 + 10
                  and ui.screen.get_height() / 2 - 10 < pygame.mouse.get_pos()[1] < ui.screen.get_height() / 2 + 10):
                hasFirstUp = True
                etat.score -= 20
                etat.init_autocliqueur(t)
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
