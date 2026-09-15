import pygame
from UI import UI
from message import Message


class Endings:
    score: int = 0

    def __init__(self, score):
        self.score = score

    def main(self):
        message_end = Message(UI.screen)
        message_credits = Message(UI.screen)
        for event in pygame.event.get():
            if event.type == game_end:
                if self.score < 0:
                    message_end.show("Patron : Mais que faites-vous?! Je ne vous paie pas pour cela !", "Suivant")
                    message_end.show("Patron : Vous êtes renvoyé·e !", "Suivant")
                    message_end.show("VOUS AVEZ ÉTÉ RENVOYÉ·E. TOUT LE MONDE EST MORT.", "Fin")
                elif self.score < 1:
                    message_end.show("VOTRE FUSÉE N'A PAS DÉCOLLÉ.\
                    L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ", "Fin")
                elif self.score < 410000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE S'EST MALHEUREUSEMENT ÉCRASÉE, PAR MANQUE DE CARBURANT.\
                    LA VILLE DE WASHINGTON D.C. A ÉTÉ RASÉE.\
                    DE NOUVELLES ÉLECTIONS ONT ÉTÉ ORGANISÉES. SNOOP DOGG EST ÉLU AVEC 67% DES VOIX.", "Fin")
                elif self.score < 430000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE, S'EST ARRÊTÉE, ET SE PERD DANS L'ESPACE.\
                    L'ÉCLIPSE A EU LIEU. RIEN N'EST ARRIVÉ. LE MONDE EST SAUVÉ.", "Fin")
                elif self.score < 750000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A DÉVIÉ DE SA TRAJECTOIRE ET S'EST ARRÊTÉE EN ORBITE LUNAIRE.\
                    DES HABITANTS DE LA LUNE ONT FAIT REPARTIR LA FUSÉE VERS LA TERRE.\
                    TOUT LE MONDE EST MORT.", "Fin")
                elif self.score < 999999999:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A LÉGÈREMENT DÉVIÉ DE SA TRAJECTOIRE ET SE DIRIGE VERS LE SOLEIL.\
                    LE SOLEIL EXPLOSE.\
                    8 MINUTES PLUS TARD, TOUT LE MONDE EST MORT.", "Fin")
                elif self.score == 1000000000:
                    message_end.show("VOTRE FUSÉE A DÉCOLLÉ. ELLE A ATTEINT SA CIBLE. LA LUNE EXPLOSE.\
                    LES DÉBRIS DE LA LUNE RETOMBENT SUR LA TERRE.\
                    TOUT LE MONDE EST MORT.", "Fin")
                else:
                    message_end.show("undefined Fin", "Undefined")
            break
        message_credits.show("Jeu réalisé dans le cadre de la SAE5.01: GameJam, du BUT Informatique, à l'université Grenoble-Alpes.\
                                Création : équipe des croustiflambs (le b est muet)\
                                Programmation : Célia MOULIN, Alenia LEFOYER, Yvan GIORDANO, Timothée DAGAND\
                                Assets graphiques : Emma DHOURY\
                                Sons : \
                                Remerciements :\
                                Merci à Jean-Pierre CHEVALLET pour son cours sur le langage Python et ses conseils lors du développement,\
                                Merci à l'équipe enseignante du BUT Informatique de l'université Grenoble-Alpes,\
                                Enfin, merci à vous d'avoir joué !\
        ", "Quitter")