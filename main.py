import math

import pygame
from UI import UI
from message import Message

from src.modele.etat import Etat

def main():
    # Démarre le module
    pygame.init()

    ui = UI()

    message = Message(ui.screen)
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

    # Boucle de l'animation
    while running:
        dt = clock.tick(60)
        t += dt

        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
