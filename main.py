import math
import events
import pygame
from UI import UI
from message import Message

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
    score = 0
    moon_angle = -math.pi / 2

    # Boucle de l'animation
    while running:
        # Fin du jeu n°1 (réservoir plein)
        if score >= 1000000000000000:
            pygame.event.post(events.GAME_END)

        # Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Fin du jeu n°2 (fenêtre cassée)
            if event.type == events.WINDOW_BREAK:
                score = -1
                pygame.event.post(events.GAME_END)

            if message.active:
                message.handle_event(event)
                continue

            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Clic bouton fuëlle
                if ui.check_mouse_position_fuelle_button():
                    ui.display_button_down()
                    score += 1
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
