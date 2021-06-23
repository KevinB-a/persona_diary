import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

class Message():
    """ """

    def __init__(self, data=False):
        self.text = None
        self.date = None
        self.id_client = None
        if data:
            self.hydrate(data)

    def hydrate(self, data):
        """ """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_message(self):
        """ """
        return """_____________________________
        text : {} \n\
        date : {} \n\
        id_client : {} \n\
        """.format(self.name, self.last_name, self.text ) 