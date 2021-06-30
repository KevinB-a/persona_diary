import sys

sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

import streamlit as st

def app2():

    st.header('voici la page des messages')
    st.sidebar.title('messages')
    method = st.sidebar.radio('action :',['add', 'update', ])

    if method == 'add' : 
        st.subheader('ajouter un message')
        text = st.text_input('ecrivez votre message')
        date = st.text_input('ecrivez la date de votre message')
        id_client = st.text_input('ecrivez l\'id du client')

    elif method == 'update' :
        st.subheader('ajouter un message')
        text = st.text_input('ecrivez votre message')
        date = st.text_input('ecrivez la date de votre message')
        id_client = st.text_input('ecrivez l\'id du client')
        id_message = st.text_input('ecrivez l\'id du message')



    #list_of_message_values = [text, date, id_message, id_client]