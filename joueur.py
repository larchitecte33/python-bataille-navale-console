from asyncio.windows_events import NULL


from case import Case
from plateau import Plateau

class Joueur:
    # Constructeur
    def __init__(self, nom):
        self.__nom = nom
        self.__plateau = NULL

    def attribuer_plateau(self):
        nb_lignes = 10
        nb_colonnes = 10

        cases = []

        for i in range(nb_lignes):
            ligne = []

            for j in range(nb_colonnes):
                c = Case(i,j)
                ligne.append(c)

            cases.append(ligne)

        p = Plateau(cases, nb_lignes, nb_colonnes)
        self.__plateau = p

    def afficherPlateau(self):
        self.__plateau.afficher()
        print('')

    def attaquer(self, x, y):
        self.__plateau.get_case(x, y).set_touchee(True)

    def placer_bateau(self, x_deb, y_deb, x_fin, y_fin):
        print('On place le bateau')

    def choisir_emplacement_bateaux(self, bateaux):
        for bateau in bateaux:
            print('Veuillez choisir l\'emplacement du ', bateau.get_nom(), ' de longueur ', bateau.get_longueur())
            emplacement = input()