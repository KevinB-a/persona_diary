import mysql.connector
import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")
from conf.id_mysql import username, password, database

class Connection():
    """Class to manage the connection and the cursor to a database"""
    # Store the username, the port and the database name as class attributs
    # In this case no host name and password because of my own configuration
    USER = username
    PASSWORD = password
    DATABASE = database
    
    def __init__(self):
        # The class stores an instance of mysql connection and cursor classes
        self.connection = None
        self.cursor = None    
    
    def initialize_connection(self):
        """Instanciate a connection and a cursor and store them in the related attributs"""
        try:
            self.connection = mysql.connector.connect(user = Connection.USER,
                                               password = Connection.PASSWORD,
                                               database = Connection.DATABASE)
            self.cursor = self.connection.cursor(buffered= True)
        except (Exception, mysql.connector.Error) as error :
            print ("Error while connecting to MySQL", error)    
   
    def close_connection(self):
        """Close both connection and cursor"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()