import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from model.connexion import Connection


class ClientModel():
    """Class to perform all queries related to the message table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()

    def show_clients(self):
        """method to display all of the clients """
        sql = "SELECT * FROM client ;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        clients = self.db.cursor.fetchall()
        self.db.close_connection()
        return clients

    def display_one_client(self, name, last_name):
        """method to dislay one client  """
        sql = "SELECT * FROM client WHERE name = %s AND last_name = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (name, last_name))
        client = self.db.cursor.fetchfetchone()
        self.db.close_connection()
        return client

    def add_client(self,name, last_name, email, date_of_birth):
        """add a new client in the database """
        sql = "INSERT INTO client(name, last_name,email , date_of_birth) VALUES(%s, %s, %s, %s);"
        percent_s = (name, last_name, email, date_of_birth )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, percent_s)
        self.db.connection.commit()
        self.db.close_connection()


    def update_client(self, name, last_name, email, date_of_birth, name2, last_name2):
        """function for update the data of a client """
        sql = "UPDATE client SET name = %s, last_name = %s, email = %s, date_of_birth = %s WHERE name = %s and last_name = %s;"  
        percent_s =(name, last_name, email, date_of_birth, name2, last_name2)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,percent_s)
        self.db.connection.commit()
        self.db.close_connection()