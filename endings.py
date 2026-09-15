import pygame
import message

class Endings:
    score: int = 0

    def __init__(self, score):
        self.score = score

    def main(self):
        messageEnd = Message(16)
        for event in pygame.event.get():
            if event.type == gameEnd:
                if self.score < 0:
                    messageEnd.print("Fin renvoi")
                    pygame.quit()
                elif score < 10000000:
                    messageEnd.print("Fin Blanchon")
                    pygame.quit()
                elif score < 410000000:
                    messageEnd.print("Fin Snoop Dogg")
                    pygame.quit()
                elif score < 430000000:
                    messageEnd.print("Bonne fin")
                    pygame.quit()
                elif score < 750000000:
                    messageEnd.print("Fin invasion")
                    pygame.quit()
                elif score < 999999999:
                    messageEnd.print("Fin solaire")
                    pygame.quit()
                elif score == 1000000000:
                    messageEnd.print("Fin lunaire")
                    pygame.quit()
                else:
                    messageEnd.print("undefined Fin")
                    pygame.quit()