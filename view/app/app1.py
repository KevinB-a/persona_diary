import sys

sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

import streamlit as st
def app1():

    st.header('voici la page des clients')
    st.sidebar.title('clients')
    method = st.sidebar.radio('action :',['add', 'update', 'delete'])

    if method == 'add' : 
        st.subheader('ajouter un client')
        name = st.text_input('ecrivez le prénom du client')
        last_name = st.text_input('ecrivez le nom du client')
        email = st.text_input('ecrivez l\'email du client')
        date_of_birth = st.text_input('ecrivez la date de naissance du client')

    elif method == 'update' :
        st.subheader('ajouter un client')
        name = st.text_input('ecrivez le prénom du client')
        last_name = st.text_input('ecrivez le nom du client')
        email = st.text_input('ecrivez l\'email du client')
        date_of_birth = st.text_input('ecrivez la date de naissance du client')
        id_client = st.text_input('ecrivez l\'id du client ')

    elif method == 'delete' :
        id_client = st.text_input('ecrivez l\'id du client ')

    #list_of_client_values = [name, last_name, email, date_of_birth, id_client]