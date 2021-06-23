import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from model.connexion import Connection

from model.message import Message


class MessageModel():
    """Class to perform all queries related to the message table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()

    def show_messages(self):
        """method to display all the message of the day """
        sql = "SELECT * FROM message LEFT JOIN client ON message.id_client = client.id_client ;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,)
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(messages):
            messages[key] = Message(value)
        return messages

    def display_one_message(self, name, last_name):
        """method to dislay one messsge  """
        sql = "SELECT * FROM message LEFT JOIN client ON message.id_client = client.id_client WHERE client.name = %s AND client.last_name = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (name,last_name))
        message = self.db.cursor.fetchone()
        self.db.close_connection()
        if message:
            return Message(message)
        return False

    def add_message(self, text, date, id_client):
        """ function for add a new message """
        sql = "INSERT INTO message (text, date , id_client) VALUES(%s, %s, %s);"
        percent_s = (text,date, id_client,) 
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()


    def update_message(self, text, date):
        """function for updating a message"""
        sql = "UPDATE message SET text = %s date = %s WHERE id_message = %s;"
        percent_s =(text,date)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,percent_s)
        self.db.connection.commit()
        self.db.close_connection()