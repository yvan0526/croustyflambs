import pygame
import message

class Endings:
    def main(self):
        for event in pygame.event.get():
            if event.type == gameEnd:
                if windowBroken == True:
                    display(Message("Fin renvoi"))
                elif score < 10000000:
                    display(Message("Fin Blanchon"))
                elif score < 410000000:
                    display(Message("Fin Snoop Dogg"))
                elif score < 430000000:
                    display(Message("Bonne fin"))
                elif score < 750000000:
                    display(Message("Fin invasion"))
                elif score < 999999999:
                    display(Message("Fin solaire"))
                elif score == 1000000000:
                    display(Message("Fin lunaire"))
                else:
                    display(Message("Erreur : Fin non définie"))