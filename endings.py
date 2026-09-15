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
                    messageEnd.print("Patron : Mais que faites-vous?! Vous n'êtes pas payé·e pour cela !")
                    messageEnd.print("Patron : Vous êtes renvoyé·e !")
                    messageEnd.print("VOUS AVEZ ÉTÉ RENVOYÉ·E. TOUT LE MONDE EST MORT.")
                    pygame.quit()
                elif score < 10000000:
                    messageEnd.print("VOTRE FUSÉE N'A PAS DÉCOLLÉ.")
                    messageEnd.print("L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ")
                    pygame.quit()
                elif score < 410000000:
                    messageEnd.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE S'EST MALHEUREUSEMENT ÉCRASÉE, PAR MANQUE DE CARBURANT.")
                    messageEnd.print("LA VILLE DE WASHINGTON D.C. A ÉTÉ RASÉE.")
                    messageEnd.print("DE NOUVELLES ÉLECTIONS ONT ÉTÉ ORGANISÉES. SNOOP DOGG EST ÉLU AVEC 67% DES VOIX.")
                    pygame.quit()
                elif score < 430000000:
                    messageEnd.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE, S'EST ARRÊTÉE, ET SE PERD DANS L'ESPACE.")
                    messageEnd.print("L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ.")
                    pygame.quit()
                elif score < 750000000:
                    messageEnd.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE ET S'EST ARRÊTÉE EN ORBITE LUNAIRE.")
                    messageEnd.print("DES HABITANTS DE LA LUNE ONT FAIT REPARTIR LA FUSÉE VERS LA TERRE.")
                    messageEnd.print("TOUT LE MONDE EST MORT.")
                    pygame.quit()
                elif score < 999999999:
                    messageEnd.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A LÉGÈREMENT DÉVIÉ DE SA TRAJECTOIRE ET SE DIRIGE VERS LE SOLEIL.")
                    messageEnd.print("LE SOLEIL EXPLOSE")
                    messageEnd.print("8 MINUTES PLUS TARD, TOUT LE MONDE EST MORT.")
                    pygame.quit()
                elif score == 1000000000:
                    messageEnd.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A ATTEINT SA CIBLE. LA LUNE EXPLOSE.")
                    messageEnd.print("LES DÉBRIS DE LA LUNE RETOMBENT SUR LA TERRE.")
                    messageEnd.print("TOUT LE MONDE EST MORT.")
                    pygame.quit()
                else:
                    messageEnd.print("undefined Fin")
                    pygame.quit()