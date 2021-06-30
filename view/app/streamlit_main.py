import sys
sys.path.insert(0,'/home/apprenant/simplon_project/personal_diary')
import streamlit as st
from view.app.app1 import app1
from view.app.app2 import app2 

PAGES = {
    "App1": app1,
    "App2": app2
        }
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
#page.app()

if selection == 'App1' : 
    app1()

else : 
    app2()