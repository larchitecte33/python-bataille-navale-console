import socket
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
    clients[0].recv(1024)
    print('Validation reçue pour le joueur 1')

    print('En attente de la validation du placement des bateaux pour le joueur 2 ...')
    clients[1].recv(1024)
    print('Validation reçue pour le joueur 2')

def jouer():
    num_joueur = 1

    while True:
        broadcast(str(num_joueur))
        
        position_tir = clients[num_joueur - 1].recv(1024)

        if num_joueur == 1:
            clients[1].recv(1024)
        else:
            clients[0].recv(1024)

        position_tir = position_tir.decode('utf-8')

        if position_tir != "-:-":
            if num_joueur == 1:
                clients[1].sendall(position_tir.encode('utf-8'))

                is_touche = clients[1].recv(1024) # Réception de l'information "touché"
                clients[0].sendall(is_touche) 
                
                if is_touche.decode('utf-8') != "C" and is_touche.decode('utf-8') != "X":
                    num_joueur = 2
            else:
                clients[0].sendall(position_tir.encode('utf-8'))

                is_touche = clients[0].recv(1024) # Réception de l'information "touché"
                clients[1].sendall(is_touche) 

                if is_touche.decode('utf-8') != "C" and is_touche.decode('utf-8') != "X":
                    num_joueur = 1


accueilirJoueurs()
jouer()
