from datetime import datetime

def reception(ma_socket, nom_client, nom_infos_a_recevoir, afficher_infos):
    if afficher_infos:
        today = datetime.now()
        print(today, 'reception ', nom_infos_a_recevoir, ' par ', nom_client, '...')
    
    infos_a_recevoir = ma_socket.recv(1024).decode('utf-8')
    
    if afficher_infos:
        print(today, nom_infos_a_recevoir, ' = ', infos_a_recevoir)

    return infos_a_recevoir

def envoi(ma_socket, nom_client, infos_a_envoyer, afficher_infos):
    if afficher_infos:
        today = datetime.now()
        print(today, 'envoi ', infos_a_envoyer, ' à ', nom_client, '...')

    ma_socket.sendall(infos_a_envoyer.encode('utf-8'))