from asyncio.windows_events import NULL

class Plateau:

    # Constructeur
    def __init__(self, cases, nb_lignes, nb_colonnes):
        self.__cases = cases
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes

    # Affichage du plateau
    def afficher(self):
        ligne = '  '

        for i in range(self.__nb_colonnes):
            if i > 0:
                ligne += ' '

            ligne += str(i)

        print(ligne)

        for j in range(self.__nb_lignes):
            ligne = str(j) + ' '
            for i in range(self.__nb_colonnes):
                if i > 0:
                    ligne += ','

                if(self.__cases[i][j].get_touchee() == True):
                    if self.__cases[i][j].get_numero_occupant() > 0:
                        ligne += 'X'
                    else:
                        ligne += '+'
                elif self.__cases[i][j].get_numero_occupant() != -1:
                    ligne += str(self.__cases[i][j].get_numero_occupant())
                else:
                    ligne += '-'
            print(ligne)
            ligne = ''
    
    # Fonction permettant de récupérer une case donnée du plateau de jeu
    # Paramètres =>
    #   i : abscisse de la case
    #   j : ordonnée de la case
    # Renvoie la case si elle existe, NULL sinon
    def get_case(self, i, j):
        if i < 0 or i >= self.__nb_lignes or j < 0 or j >= self.__nb_colonnes:
            return NULL
        else:
            return self.__cases[i][j]

    # Fonction qui détermine si une zone est libre ou non (cases non occupées)
    # Paramètres =>
    #   x_deb : abscisse de début de la zone
    #   x_fin : abscisse de fin de la zone
    #   y_deb : ordonnée de début de la zone
    #   y_fin : ordonnée de fin de la zone
    # Renvoie True si la zone est libre, False sinon
    def is_zone_libre(self, x_deb, x_fin, y_deb, y_fin):
        is_obstacle_trouve = False
        i = x_deb

        while (not is_obstacle_trouve) and i <= x_fin:
            j = y_deb

            while (not is_obstacle_trouve) and j <= y_fin:
                if self.__cases[i][j].get_numero_occupant() != -1:
                    print(i)
                    print(j)
                    is_obstacle_trouve = True

                j = j + 1
            i = i + 1

        return not is_obstacle_trouve



    # Fonction permettant de définir la position d'un bateau
    # Paramètres =>
    #   bateau : le bateau à placer
    #   x_deb : abscisse de début
    #   x_fin : abscisse de fin
    #   y_deb : ordonnée de début
    #   y_fin : ordonnée de fin
    # Retourne True si le bateau a pu être placé, False sino
    def definir_position_bateau(self, bateau, x_deb, x_fin, y_deb, y_fin):
        is_bateau_place = False
        
        try:
            x_deb_int = int(x_deb)
            x_fin_int = int(x_fin)
            y_deb_int = int(y_deb)
            y_fin_int = int(y_fin)

            if x_deb_int > x_fin_int:
                print('La position de début en x doit être inférieure ou égale à la position de fin en x')
            elif y_deb_int > y_fin_int:
                print('La position de début en y doit être inférieure ou égale à la position de fin en y')
            # Si le bateau est à la verticale
            elif x_deb_int == x_fin_int:
                if y_fin_int - y_deb_int + 1 != bateau.longueur:
                    print('Les coordonnées en Y sont inexactes.')
                elif not self.is_zone_libre(x_deb_int, x_fin_int, y_deb_int, y_fin_int):
                    print('La zone de dépose du bateau est déjà occupée.')
                else:
                    for i in range(y_deb_int, y_fin_int + 1):
                        self.__cases[x_deb_int][i].set_numero_occupant(bateau.get_numero())

                    bateau.set_x_deb(x_deb_int)
                    bateau.set_x_fin(x_fin_int)
                    bateau.set_y_deb(y_deb_int)
                    bateau.set_y_fin(y_fin_int)

                    is_bateau_place = True
            # Si le bateau est à l'horizontale
            else:
                if x_fin_int - x_deb_int + 1 != bateau.longueur:
                    print('Les coordonnées en X sont inexactes.')
                elif not self.is_zone_libre(x_deb_int, x_fin_int, y_deb_int, y_fin_int):
                    print('La zone de dépose du bateau est déjà occupée.')
                else:
                    for i in range(x_deb_int, x_fin_int + 1):
                        self.__cases[i][y_deb_int].set_numero_occupant(bateau.get_numero())

                    bateau.set_x_deb(x_deb_int)
                    bateau.set_x_fin(x_fin_int)
                    bateau.set_y_deb(y_deb_int)
                    bateau.set_y_fin(y_fin_int)

                    is_bateau_place = True

            print('VOTRE PLATEAU')
            self.afficher()
        except ValueError as inst:
            print(inst)
    
        return is_bateau_place