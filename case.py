class Case:
    # Constructeur
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__touchee = False
    
    def get_touchee(self):
        return self.__touchee

    def set_touchee(self, touchee):
        if touchee != False and touchee != True:
            print('La valeur de touchee doit être soit False, soit True')
        else:
            self.__touchee = touchee

    def get_alpha(self):
        return self.__x, ' ', self.__y