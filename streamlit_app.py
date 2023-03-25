# Display each book within a different tab or different page in multipage app
# Afficher les fables avec la fonctionnalité expander

import streamlit as st
from fables import *


st.set_page_config(
     page_title='Fables de La Fontaine',
     page_icon=':fox_face:',
     layout='wide',
     initial_sidebar_state='expanded',
 )


st.title('Les Fables de La Fontaine')

fables_all_tocs()

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

display_all_fables_all_books()

