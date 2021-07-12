
import sys

sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from fastapi import FastAPI

from model.request import *

from view.api.classes import *

from model.connection import Connection

db = Connection()

app = FastAPI()


#--------------------------------------------#
#                 user part                  #
#--------------------------------------------#


@app.get("/users/")  # request for display one client
def get_user( entry_user : User):
    cursor = db.initialize_connection()
    query ="""select * from client where id_client = %s;"""
    values = int(entry_user.user_id)
    cursor.execute(query, (values,))
    user = cursor.fetchall()
    db.close_connection()
    return {'user_id': user}


@app.put('/update_user/{user_id}') 
def update_user(entry_user : User):
    cursor, connection = db.initialize_connection()
    query = """update client set name = %s, last_name = %s, email = %s, date_of_birth = %s where id_client = %s;"""
    values = (entry_user.name, entry_user.last_name, entry_user.email, entry_user.date_of_birth, entry_user.id_client)
    cursor.execute(query, values )
    connection.commit()
    db.close_connection()
    return {'user_id' : 'mis a jour'}


@app.post('/add_user/') 
def add_user():
    cursor, connection = db.initialize_connection() 
    user_add, percent_s = add_user('name', 'last_name', 'email', '1975-02-02')
    cursor.execute(user_add, (percent_s[0], percent_s[1], percent_s[2], percent_s[3]))
    connection.commit()
    db.close_connection()
    return {'user_id' : 'user created'}



@app.delete("/delete_user/{user_id}") 
def delete_user(user_id) : 
    cursor, connection = db.initialize_connection()
    user_delete, percent_s = delete_user(user_id)
    user_id = int(user_id)
    cursor.execute(user_delete, (percent_s,))
    connection.commit()
    db.close_connection()
    return {'user_id': 'client supprimé'}
#--------------------------------------------#
#               message part                 #
#--------------------------------------------#


@app.get("/messages/") 
def get_messages():
    cursor, connection = db.initialize_connection()
    message = select_messages()
    cursor.execute(message)
    messages1 = cursor.fetchall()
    db.close_connection()
    return {'messages' : messages1}


@app.get("/message/{message_id}") 
def get_message(message_id):
    cursor, connection = db.initialize_connection()
    message_id = int(message_id)
    message, percent_s = select_message(message_id)
    cursor.execute(message, (message_id,))
    message1 = cursor.fetchall()
    db.close_connection()
    return {'message' : message1}

@app.put("/update_message/{message_id}")
def to_update_message(message_id):
    cursor, connection = db.initialize_connection()
    message_id = int(message_id)
    message_update, percent_s = update_message('je suis malheureux', message_id)
    cursor.execute(message_update, (percent_s[0], percent_s[1]))
    connection.commit()
    db.close_connection()
    return {'message' : 'le message est mis a jour'}

@app.post("/new_message/")
def new_message():
    cursor, connection = db.initialize_connection()
    user_add, percent_s = add_message('voici du texte pour meubler je le modifierais plus tard', '2021-06-29', 4 )
    cursor.execute(user_add, (percent_s[0], percent_s[1], percent_s[2]))
    connection.commit()
    db.close_connection()
    return {'user_id' : 'message successfully created'}


