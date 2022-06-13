class Bateau:
    # Constructeur
    def __init__(self, longueur, nom, numero):
        self.x_deb = -1
        self.y_deb = -1 
        self.x_fin = -1 
        self.y_fin = -1
        self.longueur = longueur
        self.nom = nom
        self.is_coule = False
        self.numero = numero

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_nom(self):
        return self.nom

    def get_longueur(self):
        return self.longueur

    def get_coule(self):
        return self.is_coule

    def set_coule(self, coule):
        self.is_coule = coule

    def set_x_deb(self, x_deb):
        self.x_deb = x_deb

    def get_x_deb(self):
        return self.x_deb

    def set_y_deb(self, y_deb):
        self.y_deb = y_deb

    def get_y_deb(self):
        return self.y_deb

    def set_x_fin(self, x_fin):
        self.x_fin = x_fin

    def get_x_fin(self):
        return self.x_fin

    def set_y_fin(self, y_fin):
        self.y_fin = y_fin

    def get_y_fin(self):
        return self.y_fin