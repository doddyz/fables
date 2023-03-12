# Comments here
import re
from collections import defaultdict

from bs4 import BeautifulSoup

BASE_IMG_URL = 'https://www.gutenberg.org/cache/epub/56327/'

with open('fables.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


def fables_titles():
    title_h3s = soup.find_all('h3')
    return [title_h3.text for title_h3 in title_h3s]


# La premiere image est obtenu pour la cigale et la fourmi a l'indice 4
def get_fables_images():
    
    image_urls = []
    chapter_divs = soup.find_all('div', class_='chapter')
    for chapter_div in chapter_divs:
        img_tag = chapter_div.find('img')
        image_urls.append(BASE_IMG_URL + img_tag['src'])
        
    return image_urls[4:]


def images_titles_dict():
    
    dico = defaultdict(str)
    titles = fables_titles()
    image_urls = get_fables_images()
    for i, image_url in enumerate(image_urls):
        dico[titles[i]] = image_url

    return dico
        



def get_fables():

    fables = {}
    titles = fables_titles()
    
    # Les fables commencent a l'index 2
    fables_divs = soup.find_all('div', class_='poem')[2:]

    for i,fable in enumerate(fables_divs):
        
        fable_div = fables_divs[i]
        fable_spans = fable_div.find_all('span')
        fable_lines = [fable_span.text for fable_span in fable_spans if re.search(r'[0-9]+$', fable_span.text) is None]
        fables[titles[i]] = fable_lines
        
    return fables 
        
        
        
    
    


    

    



