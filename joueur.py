from asyncio.windows_events import NULL


from case import Case
from plateau import Plateau

import re

class Joueur:
    # Constructeur
    def __init__(self, nom):
        self.__nom = nom
        self.__plateau = NULL
        self.__plateau_adversaire = NULL

    # Permet d'attribuer un plateau au joueur
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

        p_adversaire = Plateau(cases, nb_lignes, nb_colonnes)
        self.__plateau_adversaire = p_adversaire

    # Permet d'afficher le plateau du joueur
    def afficher_plateau(self):
        print('PLATEAU ADVERSAIRE')
        self.__plateau_adversaire.afficher()
        print('VOTRE PLATEAU')
        self.__plateau.afficher()
        print('')

    def attaquer(self, x, y):
        self.__plateau.get_case(x, y).set_touchee(True)

    # Permet au joueur de choisir l'emplacement de ses bateaux
    # Paramètres =>
    #   bateaux : les bateaux à placer
    def choisir_emplacement_bateaux(self, bateaux):
        i = 0
        quit = False
        
        while i < len(bateaux) and not quit:
            print('Veuillez choisir l\'emplacement du ', bateaux[i].get_nom(), ' de longueur ', bateaux[i].get_longueur())
            print('Format : x_deb:y_deb-x_fin:y_fin')
            print('q pour quitter')
            emplacement = input()

            if(emplacement == 'q'):
                quit = True            
            elif re.match('.:.-.:.', emplacement):
                x_deb = emplacement[0]
                y_deb = emplacement[2]
                x_fin = emplacement[4]
                y_fin = emplacement[6]
                
                if self.__plateau.definir_position_bateau(bateaux[i], x_deb, x_fin, y_deb, y_fin):
                    i = i + 1
            else:
                print('L\'emplacement fourni ne respecte pas le format x_deb:y_deb-x_fin:y_fin')
