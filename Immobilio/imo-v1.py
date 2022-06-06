
from asyncio.windows_events import NULL
from gettext import NullTranslations
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.immobilio.ma/annonces-immobilieres/?paged-1="
l = list()
pictures = list ()
pieces = list()

for page in  range(0,13) : 
    html_text = requests.get(URL + str(page) + "#catalog-listing").content
    soup = bs(html_text,'html.parser')
    ###            Partie Links             ###
    test =soup.find('div', class_='es-listing es-layout-list')

    links = test.find_all('div', class_='es-property-thumbnail')

    for cont in links :
        pictures = list ()
        pieces = list()
        try :
            link = cont.find('a').attrs['href']
        except :
            link = 'not defined'
        ###      Partie Liaison                  ###
        print(link)
        html_text2 = requests.get(link).content
        soup2 = bs(html_text2,'html.parser')    

        ###       Partie Content                 ###           
        try :
            title = soup2.find('h1', class_='entry-title').text
        except :
            title = 'not defined'
 
        test1 = soup2.find('div', class_='es-info clearfix')
        photos2 = test1.find('div', class_='es-gallery')
        photos3 = photos2.find('div', class_='es-gallery-image-pager-wrap')
        try :
            picture = photos3.find_all('div')
        except:
            picture = 'not defined'
        for pic in picture:
            try : 
                photo = pic.find('img', class_='attachment-thumbnail size-thumbnail').attrs['src']
            except :
                photo = 'not defined'
            pictures.append(photo)

        infos = test1.find('div', class_='es-property-fields')
        try:
            for f in infos.find_all('li'):
                info = f.text
                pieces.append(info)
        except:
            info = "not defined"

        # try :
        #     ref = info2[0].text
        # except:
        #     ref ='not defined'

        # try :
        #     surface = info2[1].text
        # except:
        #     surface ='not defined'

        # try :
        #     type = info2[2].text
        # except:
        #     type ='not defined'

        # try :
        #     ville = info2[3].text
        # except:
        #     ville ='not defined'

        test2 = soup2.find('div', class_='es-tabbed')
        
        try:
            caract = test2.find('div', class_='es-features-list-wrap').text
        except :
            caract ='not defined'

        desc= test2.find('div',class_='es-tabbed-item es-description')
        
        for wrapper in desc.find_all('p'):
            try :
                description=wrapper.text
            except :
                description = 'not defined'

        test3 =test2.find_all('h4')
        try :
            price =test3[0].text
        except :
            price = 'not defined'
        try:    
            tel =test3[1].text
        except:
            tel = 'not defined'

        data = {"Title":title, "photos":pictures, "Caractéristique":caract, "Description":description, "price":price, "Telephone":tel,"Pieces":pieces}

        l.append(data)



 # Storing in Excel File   
df = pd.DataFrame(l)
df.to_excel("/Users/Pro/Documents/Master MBD/MBD_S2/Web-Scraping/etl_project_Web_Scraping/immobilio/immob1-13.xlsx")



