import socket
import re
from joueur import Joueur
from bateau import Bateau
from datetime import datetime

quit = False

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

#try:
num_joueur = client.recv(1024).decode('ascii')
today = datetime.now()
print(today, 'num_joueur = ',  num_joueur)
#except:
#    print('Exception')
#    quit = True

print('reception pret_a_jouer...')
pret_a_jouer = client.recv(1024).decode('ascii')
print('pret_a_jouer = ', pret_a_jouer)

print(num_joueur, ' - Pret a jouer')

j.choisir_emplacement_bateaux(bateaux)


client.sendall(b'test')

while not quit:
    #try:
    client.sendall("P".encode('utf-8'))
    num_joueur_en_cours = client.recv(1024).decode('utf-8')

    if num_joueur_en_cours != num_joueur:
        print('Ce n\'est pas à vous de jouer')
        entree = "----"
        is_coule = False
        client.sendall(entree.encode('utf-8'))

        position_tir = client.recv(1024).decode('utf-8')

        if position_tir != "-:-":
            is_coule = j.attaquer(int(position_tir[0]), int(position_tir[2]))       

        if is_coule:
            client.sendall("C".encode('utf-8'))
        elif j.est_occupe(int(position_tir[0]), int(position_tir[2])):
            client.sendall("X".encode('utf-8'))
        else:
            client.sendall("+".encode('utf-8'))

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
            client.sendall(position_tir.encode('utf-8'))
            est_touche = client.recv(1024).decode('utf-8')

            if est_touche == "C":
                print("Coulé !!!")
                j.set_occupe(int(position_tir[0]), int(position_tir[2]))
            elif est_touche == "X":
                print("Touché !!!")
                j.set_occupe(int(position_tir[0]), int(position_tir[2]))
            else:
                print("Dans l'eau")

            j.attaquer_adversaire(int(position_tir[0]), int(position_tir[2]))

            j.afficher_plateau()

    #except:
    #    print("Une erreur est survenue")
    #    client.close()
    #    quit = True
    #    break