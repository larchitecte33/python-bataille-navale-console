from joueur import Joueur
from bateau import Bateau
from plateau import Plateau

j = Joueur('Gauthier')
j.attribuer_plateau()
j.afficher_plateau()

bateaux = []
b1 = Bateau(5, 'Porte-Avions', 1)
bateaux.append(b1)
b2 = Bateau(4, 'Croiseur', 2)
bateaux.append(b2)
b3 = Bateau(3, 'Contre-Torpilleur', 3)
bateaux.append(b3)
b4 = Bateau(3, 'Sous-Marin', 4)
bateaux.append(b4)
b5 = Bateau(2, 'Torpilleur', 5)
bateaux.append(b5)
j.choisir_emplacement_bateaux(bateaux)