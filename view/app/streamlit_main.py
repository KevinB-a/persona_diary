import sys
sys.path.insert(0,'/home/apprenant/simplon_project/personal_diary')
import streamlit as st
from view.app.app1 import app1
from view.app.app2 import app2 

PAGES = {
    "Page1": app1,
    "Page2": app2
        }
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

if selection == 'Page1' : 
    app1()

else : 
    app2()