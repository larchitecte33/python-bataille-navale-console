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
        self.__bateaux = []
        self.__cases_attaquees = []

    def get_bateaux(self): 
        return self.__bateaux

    def get_bateau(self, x, y):
        i = 0
        est_trouve = False

        print("x = ", x)
        print("y = ", y)

        while (not est_trouve) and (i < len(self.__bateaux)):
            print("x_deb = ", self.__bateaux[i].get_x_deb())
            print("x_fin = ", self.__bateaux[i].get_x_fin())
            print("y_deb = ", self.__bateaux[i].get_y_deb())
            print("y_fin = ", self.__bateaux[i].get_y_fin())

            if self.__bateaux[i].get_x_deb() >= x and self.__bateaux[i].get_x_fin() <= x and self.__bateaux[i].get_y_deb() >= y and self.__bateaux[i].get_y_fin() <= y:
                print("coucou")
                est_trouve = True
                return self.__bateaux[i]

            i = i + 1

        return NULL

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
        p.set_joueur(self)


        cases_adversaire = []

        for i in range(nb_lignes):
            ligne = []

            for j in range(nb_colonnes):
                c = Case(i,j)
                ligne.append(c)

            cases_adversaire.append(ligne)

        p_adversaire = Plateau(cases_adversaire, nb_lignes, nb_colonnes)
        self.__plateau_adversaire = p_adversaire

    # Permet d'afficher le plateau du joueur
    def afficher_plateau(self):
        print('PLATEAU ADVERSAIRE')
        self.__plateau_adversaire.afficher()
        print('VOTRE PLATEAU')
        self.__plateau.afficher()
        print('')

    # Le plateau du joueur est-il occupé en position (x, y)
    def est_occupe(self, x, y):
        return self.__plateau.get_case(x, y).get_numero_occupant() > 0

    # Permet d'occuper le plateau du joueur en position (x, y)
    def set_occupe(self, x, y):
        try:
            index = self.__cases_attaquees.index(str(x) + '-' + str(y)) 
            print('Cette case a déjé été jouée.')
        except ValueError:
            self.__plateau_adversaire.get_case(x, y).set_touchee(True)
            self.__plateau_adversaire.get_case(x, y).set_numero_occupant(1)
            self.__cases_attaquees.append(str(x) + '-' + str(y))

    # Permet de savoir si le plateau du joueur est toouché en (x, y)
    def est_touche(self, x, y):
        return self.__plateau.get_case(x, y).get_touchee()


    # Permet de réceptionner un tir sur le plateau du joueur
    # Paramètres =>
    #   x : position en x du tir
    #   y : position en y du tir
    # Renvoie True si le bateau a été coulé False sinon
    def attaquer(self, x, y):
        self.__plateau.get_case(x, y).set_touchee(True)

        is_bateau_trouve = False
        nom_bateau = ""
        i = 0
        i_bateau_coule = -1

        while (not is_bateau_trouve) and (i < len(self.__bateaux)):
            nom_bateau = self.__bateaux[i].get_nom()
            
            if x in range(self.__bateaux[i].get_x_deb(), self.__bateaux[i].get_x_fin() + 1) and y in range(self.__bateaux[i].get_y_deb(), self.__bateaux[i].get_y_fin() + 1):
                if self.__bateaux[i].get_x_deb() == self.__bateaux[i].get_x_fin(): # Bateau à la verticale
                    is_bateau_trouve = True
                    i_bateau_coule = i
                    
                    for j in range(self.__bateaux[i].get_y_deb(), self.__bateaux[i].get_y_fin() + 1):
                        if not self.__plateau.get_case(self.__bateaux[i].get_x_deb(), j).get_touchee():
                            is_bateau_trouve = False
                else: # Bateau à l'horizontale
                    is_bateau_trouve = True
                    i_bateau_coule = i
                    
                    for j in range(self.__bateaux[i].get_x_deb(), self.__bateaux[i].get_x_fin() + 1):
                        if not self.__plateau.get_case(j, self.__bateaux[i].get_y_deb()).get_touchee():
                            is_bateau_trouve = False

            i = i + 1

        if is_bateau_trouve:
            self.__bateaux[i_bateau_coule].set_coule(True)
            print("Votre ", nom_bateau, " a été coulé !!!")
            return True
        return False

    def verif_perdu(self):
        perdu = True
        i = 0

        while perdu and (i < len(self.__bateaux)):
            if not self.__bateaux[i].get_coule():
                perdu = False

            i = i + 1

        return perdu
        

    # Permet d'afficher un tir sur le plateau de l'adversaire
    # Paramètres =>
    #   x : position en x du tir
    #   y : position en y du tir
    def attaquer_adversaire(self, x, y):
        self.__plateau_adversaire.get_case(x, y).set_touchee(True)

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
                    self.__bateaux.append(bateaux[i])
                    i = i + 1
            else:
                print('L\'emplacement fourni ne respecte pas le format x_deb:y_deb-x_fin:y_fin')
