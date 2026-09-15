# Classe prenant en charge l'autocliqueur. La fréquence, la valeur et le nombre d'autocliqueurs
# peuvent éventuellement changer.
class Autocliqueur:
    cps: int
    valeur: int
    quantite: int
    nb_tot_clics: int
    temps_premier: int

    def __init__(self):
        self.cps = 0
        self.valeur = 1
        self.quantite = 1
        self.nb_tot_clics = 0
        self.temps_premier = -1
