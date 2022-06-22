import socket
import envoi_reception
from datetime import datetime

host = '127.0.0.1'                                                      
port = 6535    
num_joueur = 1

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               
server.listen()

def broadcast(message):                                                 
    for client in clients:
        client.send(message.encode('utf-8'))

def accueilirJoueurs():
    nb_joueurs = 0

    while nb_joueurs < 2:
        client, address = server.accept()
        nb_joueurs = nb_joueurs + 1
        today = datetime.now()
        print(today, ' - nb_joueurs = ', str(nb_joueurs))
        client.send(str(nb_joueurs).encode('utf-8'))
        clients.append(client)

    broadcast("Vous etes deux. La partie va commencer.")

    print('En attente de la validation du placement des bateaux pour le joueur 1 ...')
    
    envoi_reception.reception(clients[0], 'joueur1', 'validation_placement_bateaux_1', True)
    print('Validation reçue pour le joueur 1')

    print('En attente de la validation du placement des bateaux pour le joueur 2 ...')
    
    envoi_reception.reception(clients[1], 'joueur2', 'validation_placement_bateaux_2', True)
    print('Validation reçue pour le joueur 2')

def jouer():
    num_joueur = 1

    while True:
        envoi_reception.reception(clients[0], 'joueur1', 'message_client_0', True)
        envoi_reception.reception(clients[1], 'joueur2', 'message_client_1', True)
        
        envoi_reception.envoi(clients[1], 'joueur2', str(num_joueur), True)
        envoi_reception.envoi(clients[0], 'joueur1', str(num_joueur), True)
        
        position_tir = envoi_reception.reception(clients[num_joueur - 1], 'joueur' + str(num_joueur), 'position_tir', True)

        if num_joueur == 1:
            envoi_reception.reception(clients[1], 'joueur2', 'ping', True)
        else:
            envoi_reception.reception(clients[0], 'joueur1', 'ping', True)

        if position_tir != "-:-":
            if num_joueur == 1:
                envoi_reception.envoi(clients[1], 'joueur2', position_tir, True)

                is_touche = envoi_reception.reception(clients[1], 'joueur2', 'is_touche', True) # Réception de l'information "touché"

                envoi_reception.envoi(clients[0], 'joueur1', is_touche, True) 
                
                if is_touche != "C" and is_touche != "X" and is_touche != "T":
                    num_joueur = 2
            else:
                envoi_reception.envoi(clients[0], 'joueur1', position_tir, True)

                is_touche = envoi_reception.reception(clients[0], 'joueur1', 'is_touche', True) # Réception de l'information "touché"

                envoi_reception.envoi(clients[1], 'joueur2', is_touche, True)

                if is_touche != "C" and is_touche != "X" and is_touche != "T":
                    num_joueur = 1


accueilirJoueurs()
jouer()
