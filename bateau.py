class Bateau:
    # Constructeur
    def __init__(self, longueur, nom):
        self.x_deb = -1
        self.y_deb = -1 
        self.x_fin = -1 
        self.y_fin = -1
        self.longueur = longueur
        self.nom = nom
        self.is_coule = False
        self.numero = -1

    def get_numero(self):
        return self.numero

    def get_nom(self):
        return self.nom

    def get_longueur(self):
        return self.longueur