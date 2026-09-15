import pygame
import message

class Endings:
    def main(self):
        messageEnd = Message(16)
        for event in pygame.event.get():
            if event.type == gameEnd:
                if windowBroken == True:
                    messageEnd.print("Fin renvoi")
                elif score < 10000000:
                    messageEnd.print("Fin Blanchon")
                elif score < 410000000:
                    messageEnd.print("Fin Snoop Dogg")
                elif score < 430000000:
                    messageEnd.print("Bonne fin")
                elif score < 750000000:
                    messageEnd.print("Fin invasion")
                elif score < 999999999:
                    messageEnd.print("Fin solaire")
                elif score == 1000000000:
                    messageEnd.print("Fin lunaire")
                else:
                    messageEnd.print("undefined Fin")