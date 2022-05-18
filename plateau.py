from asyncio.windows_events import NULL

class Plateau:

    # Constructeur
    def __init__(self, cases, nb_lignes, nb_colonnes):
        self.__cases = cases
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes

    def afficher(self):
        #print(self.__cases[0][0].get_alpha())
        #print(self.__cases[0][1].get_alpha())
        
        for i in range(self.__nb_lignes):
            ligne = ''
            for j in range(self.__nb_colonnes):
                if j > 0:
                    ligne += ','

                if(self.__cases[i][j].get_touchee() == True):
                    ligne += 'X'
                else:
                    ligne += '-'
            print(ligne)
            ligne = ''
    
    def get_case(self, i, j):
        if i < 0 or i >= self.__nb_lignes or j < 0 or j >= self.__nb_colonnes:
            return NULL
        else:
            return self.__cases[i][j]

    def is_zone_libre(self, x_deb, x_fin, y_deb, y_fin):
        is_obstacle_trouve = False
        i = x_deb

        while (not is_obstacle_trouve) and i <= x_fin:
            j = y_deb

            while (not is_obstacle_trouve) and j < y_fin:
                if self.__cases[i][j] != '-':
                    is_obstacle_trouve = True

        return not is_obstacle_trouve
                

    def definir_position_bateau(self, bateau, x_deb, x_fin, y_deb, y_fin):
        if x_deb > x_fin:
            print('La position de début en x doit être inférieure ou égale à la position de fin en x')
        elif y_deb > y_fin:
            print('La position de début en x doit être inférieure ou égale à la position de fin en x')
        # Si le bateau est à la verticale
        elif x_deb == x_fin:
            if y_fin - y_deb + 1 != bateau.longueur:
                print('Les coordonnées en Y sont inexactes.')
            elif not self.is_zone_libre(x_deb, x_fin, y_deb, y_fin):
                print('La zone de dépose du bateau est déjà occupée.')
            else:
                for i in range(y_deb, y_fin):
                    self.__cases[x_deb][i] = bateau.get_numero()
        # Si le bateau est à l'horizontale
        else:
            if x_fin - x_deb + 1 != bateau.longueur:
                print('Les coordonnées en X sont inexactes.')
            elif not self.is_zone_libre(x_deb, x_fin, y_deb, y_fin):
                print('La zone de dépose du bateau est déjà occupée.')
            else:
                for i in range(x_deb, x_fin):
                    self.__cases[i][y_deb] = bateau.get_numero()

    