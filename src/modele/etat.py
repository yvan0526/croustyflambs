from src.modele.autocliqueur import Autocliqueur

# Classe gérant le score et les améliorations
class Etat:
    score: int
    clic_droit_debloque: bool
    valeur_clic: int
    PRIX_AMELIORATION = (10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10, "MAX")
    autocliqueur: Autocliqueur
    STAGIAIRE_MAX_APPEL = 5
    COFFEE_BOOST_DURATION = 5000


    def __init__(self):
        self.score = 0
        self.clic_droit_debloque = False
        self.valeur_clic = 1
        self.autocliqueur = Autocliqueur()
        self.stagiaire_appel = 0
        self.coffee_boost_end = 0

    # Méthode gérant un clic sur le bouton principal
    def clic(self)-> None :
        self.score += self.valeur_clic

    # Méthode gérant un clic automatique
    def clic_auto(self)-> None :
        if self.autocliqueur.quantite > 0:
            self.score += self.autocliqueur.valeur * self.autocliqueur.quantite
            self.autocliqueur.nb_tot_clics += 1

    # Méthode gérant l'amélioration du clic droit
    def debloque_clic_droit(self)-> None :
        if self.peut_debloquer_clic_droit():
            self.score -= 1000
            self.clic_droit_debloque = True
    # Vérifie la possibilité d'améliorer le clic droit
    def peut_debloquer_clic_droit(self)-> bool :
        return not self.clic_droit_debloque and self.score >= 1000

    # Méthode gérant l'amélioration de la valeur d'un clic
    def add_valeur_clic(self, bonus: int = 1)-> None :
        if self.peut_add_valeur_clic():
            self.score -= self.PRIX_AMELIORATION[self.valeur_clic]
            self.valeur_clic += bonus
    # Vérifie la possibilité d'améliorer la valeur du clic
    def peut_add_valeur_clic(self)-> bool :
        return self.valeur_clic < 10 and self.score >= self.PRIX_AMELIORATION[self.valeur_clic]

    # Méthode gérant l'amélioration de la valeur de l'autoclic
    def add_autoclic_val(self, bonus: int = 1)-> None :
        if self.peut_add_autoclic_val():
            self.score -= self.PRIX_AMELIORATION[self.autocliqueur.valeur]
            self.autocliqueur.valeur += bonus
    # Vérifie la possibilité d'améliorer la valeur de l'autoclic
    def peut_add_autoclic_val(self)-> bool :
        return (self.autocliqueur.quantite > 0
                and self.autocliqueur.valeur < 10
                and self.score >= self.PRIX_AMELIORATION[self.autocliqueur.valeur])

    # Méthode gérant l'amélioration de la fréquence de l'autoclic
    def add_autoclic_cps(self, bonus: int = 1)-> None :
        if self.peut_add_autoclic_cps():
            self.score -= self.PRIX_AMELIORATION[self.autocliqueur.cps]
            self.autocliqueur.cps += bonus
    # Vérifie la possibilité d'améliorer la fréquence de l'autoclic
    def peut_add_autoclic_cps(self)-> bool :
        return (self.autocliqueur.quantite > 0
                and self.autocliqueur.cps < 10
                and self.score >= self.PRIX_AMELIORATION[self.autocliqueur.cps])

    # Méthode gérant l'amélioration du nombre d'autocliqueurs
    def add_autocliqueur(self, t: int, bonus: int = 1)-> None :
        if self.peut_add_autocliqueur():
            if self.autocliqueur.quantite == 0:
                self.autocliqueur.temps_premier = t
            self.score -= self.PRIX_AMELIORATION[self.autocliqueur.quantite]
            self.autocliqueur.quantite += bonus
    # Vérifie la possibilité d'améliorer le nombre d'autocliqueurs
    def peut_add_autocliqueur(self)-> bool :
        return self.autocliqueur.quantite < 10 and self.score >= self.PRIX_AMELIORATION[self.autocliqueur.quantite]

    # Méthode gérant l'appel au stagiaire
    def appeler_stagiaire(self, t: int) -> None:
        if self.peut_appeler_stagiaire():
            self.stagiaire_appel += 1
            self.coffee_boost_end = t + self.COFFEE_BOOST_DURATION

    # Vérifie la possibilité d'appeler le stagiaire
    def peut_appeler_stagiaire(self) -> bool:
        return self.stagiaire_appel < self.STAGIAIRE_MAX_APPEL

    # Vérifie si le café est en train de booster le clic
    def coffee_actif(self, t: int) -> bool:
        return t < self.coffee_boost_end

    # Vérifie si la trappe est à fermer
    def stagiaire_epuise(self) -> bool:
        return self.stagiaire_appel >= self.STAGIAIRE_MAX_APPEL

    # Nombre d'appels au stagiaire restants
    def appels_stagiaire_restants(self) -> int:
        return self.STAGIAIRE_MAX_APPEL - self.stagiaire_appel