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

tab1, tab2, tab3 = st.tabs([f"**Livre 1**", f"**Livre 2**", f"**Livre 3**"])
tab4, tab5, tab6 = st.tabs([f"**Livre 4**", f"**Livre 5**", f"**Livre 6**"])
# tab1, tab2, tab3 = st.tabs([f"**Livre 1**", f"**Livre 2**", f"**Livre 3**"])
# tab1, tab2, tab3 = st.tabs([f"**Livre 1**", f"**Livre 2**", f"**Livre 3**"])



# fables_all_tocs()

# st.write('\n')
# st.write('\n')
# st.write('\n')
# st.write('\n')

# display_all_fables_all_books()

with tab1:
    fables_toc(1)
    display_fables_in_book(1)

with tab2:
    fables_toc(2)
    display_fables_in_book(2)

with tab3:
    fables_toc(3)
    display_fables_in_book(3)

with tab4:
    fables_toc(4)
    display_fables_in_book(4)

with tab5:
    fables_toc(5)
    display_fables_in_book(5)

with tab6:
    fables_toc(6)
    display_fables_in_book(6)


