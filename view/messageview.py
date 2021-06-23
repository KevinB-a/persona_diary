import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from model.messagemodel import MessageModel

from model.message import Message

from model.client import Client

import datetime

class MessageView():
    """ """
    def __init__(self):
        self.client = Client()
        self.model = MessageModel()
        self.message = Message()

    def to_show_messages(self):
        """display messages on a given date """
        messages = self.model.show_messages()
        print('voici tous les messages de vos clients')
        if messages:
            for message in messages:
                print(message)
        else:
            print("pas de messages :")
        input("Tapez sur une touche pour continuer :")

    def to_display_one_message(self):
        """function to dislay one message  """
        self.client.name = input('entrez le prénom du client :')
        self.client.last_name = input('entrez le nom du client :')
        self.model.display_one_message(self.client.name, self.client.last_name)
        print('voici le message que vous voulez voir')

    def new_message(self):
        """function for create a new message """ 
        self.message.text = input('entrez votre text : ')
        self.message.id_client = input('entrez l\'id du client : ')
        self.message.date = input('Date (jj/mm/aaaa) : ')
        self.model.add_message(self.message.text, self.message.date, self.message.id_client)

    def to_update_message(self):
        """function to update message """
        self.message.text = input('ecrivez votre text :')
        self.message.date = input('ecrivez votre date : (aaaa/mm/jj)')
        if self.message.date == '' : 
            self.message.date = datetime.now()
        self.message.update_message(self.message.text, self.message.date)
