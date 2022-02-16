# Report/resolve bug that makes get_all_fable_titles dico not to work (see update dico method in discuss.streamlit)
# Regler formattage et affichage de la fable plus agreable

import streamlit as st
from fables import *


st.set_page_config(
     page_title='Ex-stream-ly Cool App',
     page_icon='random',
     layout='wide',
     initial_sidebar_state='expanded',
 )


st.title('Les Fables de La Fontaine')

# ALL_FABLES = sorted(get_all_fable_titles())
ALL_FABLES = get_all_fable_titles_for_book(1)

# st.write(ALL_FABLES)



fable = st.sidebar.selectbox('Choisissez une fable', ALL_FABLES)

fable_container = st.expander('Fable title here', True)
with fable_container:
    st.markdown(get_fable_text(ALL_FABLES[fable]), unsafe_allow_html=True)
    # st.write(ALL_FABLES[fable])
