import sys
from google.protobuf import message
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from view.messageview import MessageView
message = MessageView()

def app():
    #--------------------------------------------#
    #            Import data                     #
    #--------------------------------------------#

    #--------------------------------------------#
    #                Header                      #
    #--------------------------------------------#
    st.title('Dataframes et les graphiques')
    #--------------------------------------------#
    #                Sidebar                     #
    #--------------------------------------------#
    st.sidebar.title('show message')
    method = st.sidebar.radio('message', ['add', 'update', 'read',])
    user_value = st.sidebar.text_input('recherche')
    st.sidebar.slider('donnez le nombre de valeurs lié à la recherche', min_value = 1 , max_value = 10)

    st.markdown('les resultats s\'affichent ici')
    #--------------------------------------------#
    #                  user_value                #
    #--------------------------------------------#
    if method == 'add' : 
        message.new_message()
        
    elif method == 'update': 
        st.dataframe()


    elif method == 'te_brut' : 
        st.dataframe()

    elif method == 'te_clean': 
        st.dataframe()
