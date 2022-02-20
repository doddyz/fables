import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup
from bs4 import *

BASE_URL = 'http://www.lesfables.fr'

BOOK_NUMBERS = '1 2 3 4 5 6 7 8 9 10 11 12'.split()

def get_all_fables_titles_dict():
    
    df = pd.read_csv('fables_titles.csv', index_col=False)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    dico = df.to_dict(orient='records')
    
    return dico

# Get all fables titles from a given book number n
def get_all_fable_titles_for_book(n):
    r = requests.get(BASE_URL + 'livre-' + str(n))
    soup = BeautifulSoup(r.content, 'html.parser')
    parent_spans = soup.find_all('span', class_='views-field views-field-title')
    child_links = [span.find('a') for span in parent_spans]
    child_link_texts = [link.text for link in child_links]
    child_link_hrefs = [link['href'] for link in child_links]

    return {link_text: BASE_URL + link_href for (link_text, link_href) in zip(child_link_texts, child_link_hrefs)}
    
# @st.cache
def get_all_fable_titles():
    dico = {}
    for i in BOOK_NUMBERS:
        dico.update(get_all_fable_titles_for_book(i))
    return dico

@st.cache
def get_fable_text(fable_url):
    r = requests.get(fable_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    parent_divs = soup.find_all('div', class_='field-item even')
    child_ps = [div.find('p') for div in parent_divs]
    child_p_texts = [p.text for p in child_ps if not(p is None)]

    return child_p_texts[0]

        
    
    
