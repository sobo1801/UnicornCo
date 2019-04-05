##Web skrapning av tripadvisor Karlskrona
#importera av paket
import requests
import bs4 as bs
import re
from pandas import DataFrame
from time import sleep

#url till sida att skrapa
url = 'https://www.tripadvisor.se/Restaurants-g189843-Karlskrona_Blekinge_County.html#EATERY_OVERVIEW_BOX'
pages = list(range(1, 40, 30))
pages = [str(i) for i in pages]


#skapa tomma listor att fylla med värden
titles = []
ratings = []
price = []


##loopa igenom alla sidor på hemsidan som ska skrapas (avgörs av range i variabeln pages)
for p in pages:
    pg = url + p
    
    #hämtar url
    response = requests.get(pg)
    
    #parse av html med beautiful soup
    tripadvisor_soup = bs.BeautifulSoup(response.text,features="html.parser")
    
    #hämta ut alla containers som innehåller den text vi vill skrapa
    restaurant_containers = tripadvisor_soup.find_all('div', class_ = 'ui_column is-9 shortSellDetails')


    #loopa containern och populera i listor
    for container in restaurant_containers:
        titles.append(container.find("a", class_ = "property_title").text)
        #restaurantCategory.append(container.find("a", class_ = "item cuisine",text=lambda text: text and "Amerikansk" in text)) #denna måste fixas. text utan id.prova ta bort det vi inte vilha
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
price_3 = ["2" if x == "$$" else x for x in price_2]
price_4 = ["3" if x == "$$ - $$$" else x for x in price_3]
price_5 = ["4" if x == "$$$" else x for x in price_4]
price_clean = price_5


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

p = figure(toolbar_location="above", plot_height=480, x_range=(0, 5.2), y_range=(-0.3,4.3))
p.circle(x='Rating', y='Price',
         source=source,
         size=20, color='navy')

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
