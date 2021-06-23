import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

class Client():
    """ class for display message  """

    def __init__(self, data=False):
        self.name = None
        self.last_name = None
        self.email = None
        self.date_of_birth = None
        if data:
            self.hydrate(data)

    def hydrate(self, data):
        """ """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_client(self):
        """ """
        return """_____________________________
        prénom : {} \n\
        nom : {} \n\
        email : {} \n\
        date_de_naissance : {} \n\
        """.format(self.name, self.last_name, self.text, self.email, self.date_of_birth) 