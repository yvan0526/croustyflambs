import pygame
import message

class Endings:
    score: int = 0

    def __init__(self, score):
        self.score = score

    def main(self):
        message_end = Message(16)
        message_credits = Message(32)
        for event in pygame.event.get():
            if event.type == gameEnd:
                if self.score < 0:
                    message_end.print("Patron : Mais que faites-vous?! Je ne vous paie pas pour cela !")
                    message_end.print("Patron : Vous êtes renvoyé·e !")
                    message_end.print("VOUS AVEZ ÉTÉ RENVOYÉ·E. TOUT LE MONDE EST MORT.")
                elif self.score < 10000000:
                    message_end.print("VOTRE FUSÉE N'A PAS DÉCOLLÉ.")
                    message_end.print("L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ")
                elif self.score < 410000000:
                    message_end.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE S'EST MALHEUREUSEMENT ÉCRASÉE, PAR MANQUE DE CARBURANT.")
                    message_end.print("LA VILLE DE WASHINGTON D.C. A ÉTÉ RASÉE.")
                    message_end.print("DE NOUVELLES ÉLECTIONS ONT ÉTÉ ORGANISÉES. SNOOP DOGG EST ÉLU AVEC 67% DES VOIX.")
                elif self.score < 430000000:
                    message_end.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE, S'EST ARRÊTÉE, ET SE PERD DANS L'ESPACE.")
                    message_end.print("L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ.")
                elif self.score < 750000000:
                    message_end.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE ET S'EST ARRÊTÉE EN ORBITE LUNAIRE.")
                    message_end.print("DES HABITANTS DE LA LUNE ONT FAIT REPARTIR LA FUSÉE VERS LA TERRE.")
                    message_end.print("TOUT LE MONDE EST MORT.")
                elif self.score < 999999999:
                    message_end.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A LÉGÈREMENT DÉVIÉ DE SA TRAJECTOIRE ET SE DIRIGE VERS LE SOLEIL.")
                    message_end.print("LE SOLEIL EXPLOSE")
                    message_end.print("8 MINUTES PLUS TARD, TOUT LE MONDE EST MORT.")
                elif self.score == 1000000000:
                    message_end.print("VOTRE FUSÉE A DÉCOLLÉ. ELLE A ATTEINT SA CIBLE. LA LUNE EXPLOSE.")
                    message_end.print("LES DÉBRIS DE LA LUNE RETOMBENT SUR LA TERRE.")
                    message_end.print("TOUT LE MONDE EST MORT.")
                else:
                    message_end.print("undefined Fin")
            break
        message_credits.print("Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\
                                Création : équipe des croustiflambs (le b est muet)\
                                Programmation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\
                                Assets graphiques : Emma DHOURY\
                                Sons : \
                                Remerciements :\
                                Merci aux enseignants blablabla toussa toussa\
                                ")