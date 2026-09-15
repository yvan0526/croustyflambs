import math

import pygame
from UI import UI
from message import Message

def main():
    # Démarre le module
    pygame.init()

    ui = UI()

    message = Message(ui.screen, ui.score_font)
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
    button_clicking = False

    # Boucle de l'animation
    while running:
        # Affiche la Lune
        ui.display_window(moon_angle)
        if moon_angle < 0:
            moon_angle += 0.001

        # Affiche la progress bar
        ui.display_progress_bar(score, 100)

        # Affiche le bureau
        ui.display_background()

        # Texte score
        ui.display_score(score)

        # Clic bouton fuëlle
        if pygame.mouse.get_pressed()[0]:
            if ui.check_mouse_position_fuelle_button():
                ui.display_button_down()
                if not button_clicking:
                    score += 1
            button_clicking = True
        else:
            button_clicking = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if message.active:
                message.handle_event(event)
                continue

        # Quitter le jeu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Mise à jour de l'affichage
        message.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
