##Web skrapning av tripadvisor Karlskrona
#importera av paket
import requests
import bs4 as bs
import re
from pandas import DataFrame
from time import sleep
from bokeh.models.tools import HoverTool
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

#url till sida att skrapa
url = 'https://www.tripadvisor.se/Restaurants-g189843-Karlskrona_Blekinge_County.html#EATERY_OVERVIEW_BOX'

#skapa tomma listor att fylla med värden
titles = []
ratings = []
price = []
    
#hämtar url
response = requests.get(url)
    
#parse av html med beautiful soup
tripadvisor_soup = bs.BeautifulSoup(response.text,features="html.parser")
    
#hämta ut alla containers som innehåller den text vi vill skrapa
restaurant_containers = tripadvisor_soup.find_all('div', class_ = 'ui_column is-9 shortSellDetails')


#loopa containern och populera i listor
for container in restaurant_containers:
    titles.append(container.find("a", class_ = "property_title").text)
    ratings.append(container.find(class_="ui_bubble_rating")["alt"])
    price.append(container.find(text=lambda text: text and "$" in text))

sleep(5)

# ta bort '\n och \n' (new line) från restaurangnamnen med strip-funktionen
titles_clean = list(map(str.strip, titles))

# gör om text "3,5 av 5 bubblor" till värdet 3,5 osv.Räkna från slutet
ratings_clean = [x[0:-13] for x in ratings]

#Gör om priskategori till skala 1,2,3 istället för $$$. Ersätt "none" med 0
price_cleanNull = ["0" if x is None else x for x in price]
price_2 = ["1" if x == "$" else x for x in price_cleanNull]
price_3 = ["2" if x == "$$ - $$$" else x for x in price_2]
price_4 = ["3" if x == "$$$$" else x for x in price_3]
price_clean = price_4


#formattera price som nummer
price_numeric = [int(i) for i in price_clean]

#byt ut kommatecken mot punkt i ratings -krävs för konvertering till float
ratings_remove_comma = [x.replace(',', '.') for x in ratings_clean ]

#formattera ratings som float
ratings_numeric = [float(i) for i in ratings_remove_comma]

#skapa en panda dataframe av de tre individuella listorna
df_konkurrenter = DataFrame({"Restaurang":titles_clean,
                        "Rating":ratings_numeric,
                        "Price":price_numeric})

#bokeh API för visualisering
print(df_konkurrenter)

#output fil för visualisering i HTML
output_file('MA_CompetitorScatterPlot.html')

source = ColumnDataSource(df_konkurrenter)

p = figure(toolbar_location="above", plot_height=480, x_range=(0, 5.2), y_range=(-0.3,3.99))
p.circle(x='Rating', y='Price',
         source=source,
         size=20, color='navy', alpha=0.3)

p.title.text = 'Jämförelse av restauranger i Karlskrona'
p.xaxis.axis_label = 'Betyg'
p.yaxis.axis_label = 'Pris'

#kod för att skapa ett hovertool
hover = HoverTool()
hover.tooltips=[
    ('Restaurang: ', '@Restaurang'),
    ('Betyg: ', '@Rating{(0.0)}'),
    ('Pris: ', '@Price'),
]


p.add_tools(hover)

#visa graf i fönster
show(p)
