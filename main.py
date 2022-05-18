from joueur import Joueur
from bateau import Bateau
from plateau import Plateau

j = Joueur('Gauthier')
j.attribuer_plateau()
j.afficherPlateau()
j.attaquer(1, 3)
j.afficherPlateau()

bateaux = []
b1 = Bateau(5, 'Porte-Avions')
bateaux.append(b1)
j.choisir_emplacement_bateaux(bateaux)