
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.immobilio.ma/annonces-immobilieres/?es_search%5Bkeywords%5D=&es_search%5Bes_category%5D%5B%5D=194"
l = list()


html_text = requests.get(URL + "#catalog-listing").content

soup = bs(html_text,'html.parser')

test =soup.find('div', class_='es-listing es-layout-list')
content = test.find_all('div', class_='es-thumbnail')
for cont in content :
    try :
        title = cont.find('a').attrs['href']

    except :
        title = 'not defined'
    print(title)



