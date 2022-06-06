
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.immobilio.ma/property/appartements-a-vendre-derb-ghallef/"
l = list()
pictures = list ()
pieces = list ()
html_text = requests.get(URL + "#catalog-listing").content
soup = bs(html_text,'html.parser')

try :
    title = soup.find('h1', class_='entry-title').text
except :
    title = 'not defined'

test1 = soup.find('div', class_='es-info clearfix')
photos2 = test1.find('div', class_='es-gallery')
photos3 = photos2.find('div', class_='es-gallery-image-pager-wrap')
picture = photos3.find_all('div')
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
print(pieces)

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


test2 = soup.find('div', class_='es-tabbed')

caract = test2.find('div', class_='es-features-list-wrap').text


desc= test2.find('div',class_='es-tabbed-item es-description')


for wrapper in desc.find_all('p'):
    desc2=wrapper.text


test3 =test2.find_all('h4')

price =test3[0].text

tel =test3[1].text



data = {"Title":title, "photos":pictures, "Caractéristique":caract, "Description":desc2, "price":price, "Telephone":tel,'Pieces':pieces}

l.append(data)



 #"Ref":ref, "Surface":surface, "Type":type, "Ville":ville,