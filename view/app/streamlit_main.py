import sys
sys.path.insert(0,'/home/apprenant/simplon_project/personal_diary')
import streamlit as st
import requests
from mysql.connector.errors import IntegrityError
import locale
from datetime import date
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
d = date.today()


st.header("Votre journal intime en ligne")
st.subheader("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(d))

selection = st.sidebar.radio("Go to", ['CRUD Client', 'CRUD message'])


if selection == 'CRUD Client' : 
    st.header('voici la page des clients')
    st.sidebar.title('clients')
    method = st.sidebar.radio('action :',['afficher','ajouter', 'modifier', 'supprimer'])

    if method == 'afficher':
        url = 'http://127.0.0.1:8000/users'
    
    elif method == 'ajouter' : 
        st.subheader('ajouter un client')
        url = 'http://127.0.0.1:8000/users/add_user'
        user_data = {}

        user_data['name'] = st.text_input('ecrivez le prénom du client')
        user_data['last_name'] = st.text_input('ecrivez le nom du client')
        user_data['email'] = st.text_input('ecrivez l\'email du client')
        user_data['date_of_birth'] = st.date_input('ecrivez la date de naissance du client')
        user_data['date_of_birth'] = str(user_data['date_of_birth'])
        submit_button = st.button('soumettre')
        if submit_button:
            try :
                #call the API with the post operation
                response = requests.post(url, json = user_data)
                #validation message if everything is alright
                if response.status_code == 200:
                    st.write("Votre texte : {}".format(user_data['text_content']))
                    st.write("Date d'entrée du texte : {}".format(user_data['text_date']))
                    #otherwise show the error which occured
                else:
                    st.write("une erreur est survenue")
                    st.write("Error:",response.status_code,response.text )

            except IntegrityError :
                st.write("Nous n\'avons pas pu vous enregistrer car vous existez déjà dans la base de données")
            except requests.ConnectionError as error:
                print(error)

    elif method == 'modifier' :
        st.subheader('ajouter un client')
        name = st.text_input('ecrivez le prénom du client')
        last_name = st.text_input('ecrivez le nom du client')
        email = st.text_input('ecrivez l\'email du client')
        date_of_birth = st.text_input('ecrivez la date de naissance du client')
        id_client = st.text_input('ecrivez l\'id du client ')

    elif method == 'supprimer' :
        id_client = st.text_input('ecrivez l\'id du client ')

else : 
    st.header('voici la page des messages')
    st.sidebar.title('messages')
    method = st.sidebar.radio('action :',['add', 'update', ])

    if method == 'add' : 
            #define the url of the API and the path of the collection we work with
        url = 'http://127.0.0.1:8081/text'

    #Define the object attributs we want to send to the API
    user_data = {}
    user_data['text_content'] = st.text_input("Veuillez renseigner votre texte")
    user_data['id_client'] = st.text_input("Veuillez renseigner l\'identifiant du client")
    user_data['text_date'] = st.date_input("Veuillez renseigner la date correspondante à votre texte",value = None, min_value = date(1900, 1, 1))
    user_data['text_date'] = str(user_data['text_date'])

    submit_button = st.button("Soumettre")


    if submit_button:
        try :
            #call the API with the post operation
            response = requests.post(url, json = user_data)
            #validation message if everything is alright
            if response.status_code==200:
                st.write("Votre texte : {}".format(user_data['text_content']))
                st.write("Date d'entrée du texte : {}".format(user_data['text_date']))
            #otherwise show the error which occured
            else:
                st.write("une erreur est survenue")
                st.write("Error:",response.status_code,response.text )

        except IntegrityError :
            st.write("Nous n\'avons pas pu vous enregistrer car vous existez déjà dans la base de données")
        except requests.ConnectionError as error:
            print(error)

    elif method == 'update' :
        st.subheader('ajouter un message')
        text = st.text_input('ecrivez votre message')
        date = st.text_input('ecrivez la date de votre message')
        id_client = st.text_input('ecrivez l\'id du client')
        id_message = st.text_input('ecrivez l\'id du message')
