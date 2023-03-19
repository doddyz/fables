# Importance de trouver la meilleur source possible a la base
# la plus simple à traiter directement

# Comments here
import re
from collections import defaultdict
from bs4 import BeautifulSoup

TITLES_PATTERN = re.compile('[A-Za-z’éàèç_\s]+[a-zéàèç]$')


with open('fables.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

def fables_titles():
    
    titles = []
    divs = soup.find_all('div', class_='title')
    for div in divs:
        for tag in div.descendants:
            if isinstance(tag, str) and re.search(TITLES_PATTERN, tag):
                titles.append(tag)
    titles = [title.strip() for title in titles]
    # 1st fable is the 4th element in this list
    return titles[4:]

# Work on text and titles at the same time
def get_fables():

    return_dico = {}

    titles = fables_titles()
    divs = soup.find_all('div', class_='linegroup')
    
    # fable divs start at index 1
    divs = divs[1:]

    # This will have to be manually adjusted as some fables have more than one linegroup div
    for i, title in enumerate(titles):
        
        lines_of_text = []
        
        for elt in divs[i]:
            
            if elt.string != '\n':
                text = str(elt.string)
                lines_of_text.append(text.strip())
                
        return_dico[title] = lines_of_text

    return return_dico
            
        
    
    
    
    
    
        
        
    
    


    

    



