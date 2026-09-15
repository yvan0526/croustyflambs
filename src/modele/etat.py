from src.modele.autocliqueur import Autocliqueur

class Etat:
    score: int
    clic_droit_debloque: bool
    valeur_clic: int
    autocliqueur: Autocliqueur

    def __init__(self):
        self.score = 0
        self.clic_droit_debloque = False
        self.valeur_clic = 1
        self.autocliqueur = Autocliqueur()

    def clic(self)-> None :
        self.score += self.valeur_clic

    def clic_auto(self)-> None :
        self.score += self.autocliqueur.valeur
        self.autocliqueur.nb_tot_clics += 1

    def debloque_clic_droit(self)-> None :
        self.clic_droit_debloque = True

    def add_valeur_clic(self, valeur: int)-> None :
        self.valeur_clic += valeur

    def init_autocliqueur(self, t: int) -> None :
        self.autocliqueur.temps_premier = t
        self.autocliqueur.cps = 1