import socket
import re
import envoi_reception
from joueur import Joueur
from bateau import Bateau
from datetime import datetime

quit = False
nb_coule = 0

print('Quel est votre nom ?')
nom_joueur = input()

j = Joueur(nom_joueur)
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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
client.connect(('127.0.0.1', 6535))

num_joueur = envoi_reception.reception(client, nom_joueur, 'num_joueur', False)
pret_a_jouer = envoi_reception.reception(client, nom_joueur, 'pret_a_jouer', False)

print(num_joueur, ' - Pret a jouer')

j.choisir_emplacement_bateaux(bateaux)

envoi_reception.envoi(client, 'serveur', 'placement_valide', False)


while not quit:
    envoi_reception.envoi(client, 'serveur', 'ping', False)

    num_joueur_en_cours = envoi_reception.reception(client, nom_joueur, 'num_joueur_en_cours', False)

    if num_joueur_en_cours != num_joueur:
        print('Ce n\'est pas à vous de jouer')
        entree = "----"
        is_coule = False
        
        envoi_reception.envoi(client, 'serveur', entree, False)

        position_tir = envoi_reception.reception(client, nom_joueur, 'position_tir', False)

        if position_tir != "-:-":
            if j.est_touche(int(position_tir[0]), int(position_tir[2])):
                envoi_reception.envoi(client, 'serveur', 'T', False)
            else:
                is_coule = j.attaquer(int(position_tir[0]), int(position_tir[2]))       

                if is_coule:
                    envoi_reception.envoi(client, 'serveur', 'C', False)
                elif j.est_occupe(int(position_tir[0]), int(position_tir[2])):
                    envoi_reception.envoi(client, 'serveur', 'X', False) 
                else:
                    envoi_reception.envoi(client, 'serveur', '+', False)

            if j.verif_perdu():
                print('Vous avez perdu.')
                quit = True

        j.afficher_plateau()
    else:
        position_tir = "-:-"

        while position_tir == "-:-":
            print('Quelle case souhaitez-vous attaquer ?')
            position_tir = input()

            if not re.match('.:.', position_tir):
                print('L\'emplacement fourni ne respecte pas le format x:y')
                position_tir = "-:-"
            elif len(position_tir) != 3:
                print('L\'emplacement fourni ne respecte pas le format x:y')
                position_tir = "-:-"
            elif(not position_tir[0].isnumeric()) or (not position_tir[2].isnumeric()):
                print('L\'emplacement fourni est invalide')
                position_tir = "-:-"
            elif (int(position_tir[0]) < 0) or (int(position_tir[0]) > 9) or (int(position_tir[2]) < 0) or (int(position_tir[2]) > 9):
                print('L\'emplacement fourni est invalide')
                position_tir = "-:-"
             

        if position_tir != "-:-":
            envoi_reception.envoi(client, 'serveur', position_tir, False)
            est_touche = envoi_reception.reception(client, nom_joueur, 'est_touche', False)

            if est_touche == "T":
                print("Cette case a déjà été attaquée.")
            elif est_touche == "C":
                print("Coulé !!!")
                j.set_occupe(int(position_tir[0]), int(position_tir[2]))
                nb_coule = nb_coule + 1

                if nb_coule >= 5:
                    print("Vous avez gagné !")
                    quit = True
            elif est_touche == "X":
                print("Touché !!!")
                j.set_occupe(int(position_tir[0]), int(position_tir[2]))
            else:
                print("Dans l'eau")

            j.attaquer_adversaire(int(position_tir[0]), int(position_tir[2]))

            j.afficher_plateau()