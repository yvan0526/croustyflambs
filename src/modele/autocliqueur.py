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

    def add_cps(self, nb: int = 1)-> None :
        self.cps += nb

    def add_valeur(self, nb: int = 1)-> None :
        self.valeur += nb

    def add_autocliqueur(self, nb: int = 1)-> None :
        self.quantite += nb