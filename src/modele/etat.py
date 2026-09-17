import math

from src.modele.autocliqueur import Autocliqueur

# Classe gérant le score et les améliorations
class Etat:
    score: int
    clic_droit_debloque: bool
    valeur_clic: int
    autocliqueur: Autocliqueur
    STAGIAIRE_MAX_APPEL = 5
    COFFEE_BOOST_DURATION = 5000
    SCORE_GOAL = 1000000000000000

    def __init__(self):
        self.score = 0
        self.clic_droit_debloque = False
        self.valeur_clic = 1
        self.autocliqueur = Autocliqueur()
        self.stagiaire_appel = 0
        self.coffee_boost_end = 0
        self.nb_upgrade_clic = 0
        self.nb_upgrade_autoclic_val = 0
        self.nb_upgrade_autoclic_cps = 0

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
    def add_valeur_clic(self, bonus: float = 1.22) -> None:
        if self.peut_add_valeur_clic():
            self.score -= self.calc_prix(self.nb_upgrade_clic, "faible")
            self.valeur_clic = math.ceil(self.valeur_clic * bonus)
            self.nb_upgrade_clic += 1
    # Vérifie la possibilité d'améliorer la valeur du clic
    def peut_add_valeur_clic(self) -> bool:
        return self.score >= self.calc_prix(self.nb_upgrade_clic, "faible")

    # Méthode gérant l'amélioration de la valeur de l'autoclic
    def add_autoclic_val(self, bonus: float = 1.18) -> None:
        if self.peut_add_autoclic_val():
            self.score -= self.calc_prix(self.nb_upgrade_autoclic_val, "faible")
            self.autocliqueur.valeur = math.ceil(self.autocliqueur.valeur * bonus)
            self.nb_upgrade_autoclic_val += 1
    # Vérifie la possibilité d'améliorer la valeur de l'autoclic
    def peut_add_autoclic_val(self) -> bool:
        return (self.autocliqueur.quantite > 0
                and self.score >= self.calc_prix(self.nb_upgrade_autoclic_val, "faible"))


    # Méthode gérant l'amélioration de la fréquence de l'autoclic
    def add_autoclic_cps(self, t: int, bonus: int = 1.18) -> None:
        if self.peut_add_autoclic_cps():
            self.score -= self.calc_prix(self.nb_upgrade_autoclic_cps, "faible")
            self.autocliqueur.cps = math.ceil(self.autocliqueur.cps * bonus)
            self.autocliqueur.temps_ref += int(
                (t - self.autocliqueur.temps_ref) / self.autocliqueur.cps
            )
            self.nb_upgrade_autoclic_cps += 1

    def peut_add_autoclic_cps(self) -> bool:
        return (
                self.autocliqueur.quantite > 0
                and self.score >= self.calc_prix(
            self.nb_upgrade_autoclic_cps, "faible"
        )
    )

    # Méthode gérant l'amélioration du nombre d'autocliqueurs
    def add_autocliqueur(self, t: int, bonus: int = 1)-> None :
        if self.peut_add_autocliqueur():
            if self.autocliqueur.quantite == 0:
                self.autocliqueur.temps_ref = t
            self.score -= self.calc_prix(self.autocliqueur.quantite, "moyen")
            self.autocliqueur.quantite += bonus
    # Vérifie la possibilité d'améliorer le nombre d'autocliqueurs
    def peut_add_autocliqueur(self)-> bool :
        return (self.autocliqueur.quantite < 10
                and self.score >= self.calc_prix(self.autocliqueur.quantite, "moyen"))

    # Calcule le prix d'une amélioration. libelle_cout peut être faible ou moyen.
    @staticmethod
    def calc_prix(nb_up: int, libelle_cout: str) -> int :
        match libelle_cout:
            case "faible":
                return int(10 * 1.25 ** nb_up)
            case "moyen":
                return 100 * 20 ** nb_up

        return -1
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
