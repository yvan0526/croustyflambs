from src.modele.autocliqueur import Autocliqueur

# Classe gérant le score et les améliorations
class Etat:
    score: int
    clic_droit_debloque: bool
    valeur_clic: int
    nb_ameliorations: int
    PRIX_AMELIORATION = (10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920, 163840, 327680)
    autocliqueur: Autocliqueur

    def __init__(self):
        self.score = 0
        self.clic_droit_debloque = False
        self.nb_ameliorations = 0
        self.valeur_clic = 1
        self.autocliqueur = Autocliqueur()

    # Méthode gérant un clic sur le bouton principal
    def clic(self)-> None :
        self.score += self.valeur_clic

    # Méthode gérant un clic automatique
    def clic_auto(self)-> None :
        self.score += self.autocliqueur.valeur
        self.autocliqueur.nb_tot_clics += 1

    # Méthode gérant l'amélioration du clic droit en vérifiant la possibilité de l'acheter
    def debloque_clic_droit(self)-> None :
        if not self.clic_droit_debloque and self.score >= 1000:
            self.score -= 1000
            self.clic_droit_debloque = True

    # Méthode gérant l'amélioration de la valeur d'un clic en vérifiant la possibilité de l'acheter
    def add_valeur_clic(self, bonus: int = 1)-> None :
        if self.valeur_clic <= 10 and self.score >= self.PRIX_AMELIORATION[self.nb_ameliorations]:
            self.valeur_clic += bonus
            self.score -= self.PRIX_AMELIORATION[self.nb_ameliorations]
            self.nb_ameliorations += 1

    # Méthode gérant la première amélioration, l'achat d'un autocliqueur. Vérifie la possibilité de l'acheter.
    def init_autocliqueur(self, t: int) -> None :
        if self.nb_ameliorations == 0 and self.score >= self.PRIX_AMELIORATION[0]:

            self.autocliqueur.quantite = 1
            self.score -= self.PRIX_AMELIORATION[0]
            self.nb_ameliorations += 1

    # Méthode gérant l'amélioration de la valeur de l'autoclic en vérifiant la possibilité de l'acheter
    def add_autoclic_val(self, bonus: int = 1)-> None :
        if self.autocliqueur.valeur <= 10 and self.score >= self.PRIX_AMELIORATION[self.nb_ameliorations]:
            self.autocliqueur.valeur += bonus
            self.score -= self.PRIX_AMELIORATION[self.nb_ameliorations]
            self.nb_ameliorations += 1

    # Méthode gérant l'amélioration de la fréquence de l'autoclic en vérifiant la possibilité de l'acheter
    def add_autoclic_cps(self, bonus: int = 1)-> None :
        if self.autocliqueur.cps <= 15 and self.score >= self.PRIX_AMELIORATION[self.nb_ameliorations]:
            self.autocliqueur.cps += bonus
            self.score -= self.PRIX_AMELIORATION[self.nb_ameliorations]
            self.nb_ameliorations += 1

    # Méthode gérant l'amélioration du nombre d'autocliqueurs en vérifiant la possibilité de l'acheter
    def add_autocliqueur(self, t: int, bonus: int = 1)-> None :
        if self.autocliqueur.quantite <= 10 and self.score >= self.PRIX_AMELIORATION[self.nb_ameliorations]:
            self.autocliqueur.quantite += bonus
            self.score -= self.PRIX_AMELIORATION[self.nb_ameliorations]
            self.nb_ameliorations += 1
            if self.nb_ameliorations == 0:
                self.autocliqueur.temps_premier = t
