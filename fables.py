# Importance de trouver la meilleur source possible a la base
# la plus simple à traiter directement

# Comments here
import re
import os
from bs4 import BeautifulSoup
import streamlit as st


# Good exercise, create all of the fables images using DALLE or better a similar
# open source/free image generation AI tool

TITLES_PATTERN = re.compile('[A-Za-z’éàèç_\s]+[a-zéàèç]$')

# 12 books in total 
def get_fables_titles(book_number):
    
    return sorted(os.listdir('html/livre-' + str(book_number)))


# Get fable's text, return as list of lines
def fable_text(book_number, fable_title):
    
    with open('html/livre-' + str(book_number) + '/' + fable_title) as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    divs = soup.find_all('div', class_= ['field-item', 'even'])

    return divs[3].p.text.split('\n')



def fables_toc(book_number):

    fables_titles = get_fables_titles(book_number)

    st.header('Livre ' + str(book_number))
    
    for fable_title in fables_titles:
        formatted_title = fable_title.capitalize().replace('-', ' ')
        st.markdown(f'##### [{formatted_title}](#{fable_title})')
    


def display_one_fable(book_number, fable_title):
    
    formatted_title = fable_title.capitalize().replace('-', ' ')
    st.subheader(f'{formatted_title}')
    st.markdown('<br>'.join(fable_text(book_number, fable_title)), unsafe_allow_html=True)


def display_fables_in_book(book_number):
    
    fables_titles = get_fables_titles(book_number)
    
    for fable_title in fables_titles:
        display_one_fable(book_number, fable_title)


    
    

            
        
    
    
    
    
    
        
        
    
    


    

    



