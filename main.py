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

    font = pygame.font.SysFont(None, 80)

    hasFirstUp: bool = False
    etat: Etat = Etat()

    moon_angle = -math.pi / 2
    button_clicking = False

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Fin réservoir plein
        if etat.score >= 1000000000000000:
            pygame.event.post(GAME_END)

        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

        # Affiche la progress bar
        ui.display_progress_bar(score, 100)

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

        # Clic bouton fuëlle
        if pygame.mouse.get_pressed()[0]:
            if ui.check_mouse_position_fuelle_button():
                ui.display_fuelle_button_down()
                if not button_clicking:
                    score += 1
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
                message_end = Message(UI.screen)
                message_credits = Message(UI.screen)
                if etat.score < 0: # Casser la fenêtre met le score à une valeur négative et termine le jeu
                    message_end.show("Patron : Mais que faites-vous?! Je ne vous paie pas pour cela !", "Suivant")
                    message_end.show("Patron : Vous êtes renvoyé·e !", "Suivant")
                    message_end.show("VOUS AVEZ ÉTÉ RENVOYÉ·E. TOUT LE MONDE EST MORT.", "Fin")
                elif etat.score < 1:
                    message_end.show("VOTRE FUSÉE N'A PAS DÉCOLLÉ.\
                    L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ", "Fin")
                elif etat.score < 410000000000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE S'EST MALHEUREUSEMENT ÉCRASÉE, PAR MANQUE DE CARBURANT.\
                    L'IUT2 DE GRENOBLE A ÉTÉ RASÉ.\
                    CÉDRIC GÉROT, S'ÉTANT RECONVERTI, EST ÉLU PRÉSIDENT DE LA RÉPUBLIQUE FRANÇAISE AVEC 69% DES VOIX.", "Fin")
                elif etat.score < 430000000000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE, S'EST ARRÊTÉE, ET SE PERD DANS L'ESPACE.\
                    L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ.", "Fin")
                elif etat.score < 750000000000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE ET S'EST ARRÊTÉE EN ORBITE LUNAIRE.\
                    DES HABITANTS DE LA LUNE ONT FAIT REPARTIR LA FUSÉE VERS LA TERRE.\
                    LA POPULATION TERRESTRE EST RÉDUITE EN ESCLAVAGE.", "Fin")
                elif etat.score < 999999999999999:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A LÉGÈREMENT DÉVIÉ DE SA TRAJECTOIRE ET SE DIRIGE VERS LE SOLEIL.\
                    LE SOLEIL EXPLOSE.\
                    8 MINUTES PLUS TARD, TOUT LE MONDE EST MORT.", "Fin")
                elif etat.score == 1000000000000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A ATTEINT SA CIBLE. LA LUNE EXPLOSE.\
                    LES DÉBRIS DE LA LUNE RETOMBENT SUR LA TERRE.\
                    TOUT LE MONDE EST MORT.", "Fin")
                else:
                    message_end.show("undefined Fin", "Undefined")
                message_credits.show("Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\
                                                Création : équipe des croustiflambs (le b est muet)\
                                                Programmation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\
                                                Assets graphiques : Emma DHOURY\
                                                Sons : \
                                                Remerciements :\
                                                Merci à Jean-Pierre CHEVALLET pour son cours sur le langage Python et ses conseils lors du développement,\
                                                Merci à l'équipe enseignante du BUT Informatique de l'université Grenoble-Alpes,\
                                                Enfin, merci à vous d'avoir joué !", "Quitter")
                pygame.quit()
                quit()

            if message.active:
                message.handle_event(event)
                continue

            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Clic bouton fuëlle
                if ui.check_mouse_position_fuelle_button():
                    ui.display_button_down()
                    etat.clic()
                elif (not (hasFirstUp) and etat.score >= 20
                  and ui.screen.get_width() / 4 - 10 < pygame.mouse.get_pos()[0] < ui.screen.get_width() / 4 + 10
                  and ui.screen.get_height() / 2 - 10 < pygame.mouse.get_pos()[1] < ui.screen.get_height() / 2 + 10):
                    hasFirstUp = True
                    etat.score -= 20
                    etat.init_autocliqueur(t)
            elif event.type == pygame.MOUSEBUTTONUP:
                ui.display_button_up()

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        message.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
