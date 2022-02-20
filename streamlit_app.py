# Fixer fables incompletes: le renard et le corbeau par exemple

import streamlit as st
from fables import *


st.set_page_config(
     page_title='Ex-stream-ly Cool App',
     page_icon=':fox_face:',
     layout='wide',
     initial_sidebar_state='expanded',
 )


st.title('Les Fables de La Fontaine')

ALL_FABLES = get_all_fables_titles_dict()

fable = st.sidebar.selectbox('Choisissez une fable', sorted(ALL_FABLES.keys()))

# fable_container = st.expander(fable, True)
fable_container = st.container()


with fable_container:
    st.header(fable)
    st.markdown(get_fable_text(ALL_FABLES[fable]), unsafe_allow_html=True)
    st.write(ALL_FABLES[fable])
