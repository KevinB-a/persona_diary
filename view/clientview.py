
import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from model.clientmodel import ClientModel

from model.client import Client


import datetime

class ClientView():
    """class for interact with user """
    def __init__(self):
        self.client = Client()
        self.model = ClientModel()

    def to_show_clients(self):
        """display all clients """
        clients = self.model.show_clients()
        print('voici tous les messages de vos clients')
        if clients:
            for client in clients:
                print(client)
        else:
            print("pas de clients :")
        input("Tapez sur une touche pour continuer :")

    def to_display_one_client(self):
        """function to dislay one message  """
        self.client.name = input('entrez le prénom du client :')
        self.client.last_name = input('entrez le nom du client :')
        self.model.display_one_client(self.client.name, self.client.last_name)
        print('voici le client que vous voulez voir')

    def new_client(self):
        """function for create a new client """ 
        self.client.name = input('entrez le prénom du client : ')
        self.client.last_name = input('entrez le nom du client : ')
        self.client.email = input('Entrez l \'email du client : ')
        self.client.date_of_birth = input('entrez la date de naissance du client :')
        self.model.add_client(self.client.name, self.client.last_name, self.client.email, self.client.date_of_birth)

    def to_update_client(self):
        """ """
        self.client.name = input('entrez le prénom du client : ')
        self.client.last_name = input('entrez le nom du client : ')
        self.client.email = input('Entrez l \'email du client : ')
        self.client.date_of_birth = input('entrez la date de naissance du client :')
        name = input('entrez le prénom du client (valeur originelle): ')
        last_name = input('entrez le nom du client (valeur originelle) : ')
        if self.message.date == '' : 
            self.message.date = datetime.now()
        self.message.update_client(self.client.name, self.client.last_name, self.client.email, self.client.date_of_birth, name, last_name)
