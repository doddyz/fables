# Fixer fables incompletes: le renard et le corbeau par exemple

import streamlit as st
from fables import *


st.set_page_config(
     page_title='Fables de La Fontaine',
     page_icon=':fox_face:',
     layout='wide',
     initial_sidebar_state='expanded',
 )


st.title('Les Fables de La Fontaine')

ALL_FABLES = get_fables()
ALL_FABLES_TITLES = sorted(fables_titles())
IMAGE_TITLES = images_titles_dict()

fable = st.sidebar.selectbox('Choisissez une fable', ALL_FABLES_TITLES, 140)

# fable_container = st.expander(fable, True)
fable_container = st.container()


with fable_container:
    
    st.header(fable)
    
    if IMAGE_TITLES[fable] != '':
        st.image(IMAGE_TITLES[fable])
        
    st.markdown('<br>'.join(ALL_FABLES[fable]), unsafe_allow_html=True)
    # st.write('\n'.join(ALL_FABLES[fable]))
