#--------------------------------------------#
#            user request                    #
#--------------------------------------------#


def display_user(id_client):
    select_user = "select * from client where id_client = %s;"
    percent_s = (id_client,)
    return select_user, percent_s


def update_user(name, last_name, email, date_of_birth, id_client):
    user_update = "update client set name = %s, last_name = %s, email = %s, date_of_birth = %s where id_client = %s;"
    percent_s = [name, last_name, email, date_of_birth,id_client]
    return user_update, percent_s


def display_users(): 
    select_users = "select * from client ;"
    return select_users


def add_user(name, last_name, email, date_of_birth) : 
    user_add = "insert into client(name, last_name, email , date_of_birth) values(%s, %s,%s, %s);"
    percent_s = [name, last_name, email, date_of_birth]
    return user_add, percent_s

def delete_user(id_client):

    user_delete = 'delete from client where id_client = %s;'
    percent_s = id_client
    return user_delete , percent_s

#--------------------------------------------#
#            message request                 #
#--------------------------------------------#
def select_messages():
    select_messages = "select * from message;"
    return select_messages


def select_message(message_id):
    select_message = "select text from message where id_message = %s;"
    percent_s = message_id
    return select_message , percent_s

def update_message(text, message_id):
    message_update = "update message set text = %s where id_message = %s;"
    percent_s = [text, message_id]
    return message_update, percent_s

def add_message(text, date, id_client):
    message_add = "insert into message (text, date , id_client) VALUES(%s, %s, %s);"
    percent_s = [text, date, id_client]
    return message_add, percent_s
