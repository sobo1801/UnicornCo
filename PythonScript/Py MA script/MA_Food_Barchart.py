##Web skrapning av tripadvisor Karlskrona
#importera av paket
import requests
import bs4 as bs
from pandas import DataFrame
from time import sleep

#url till sida att skrapa
url = 'https://www.tripadvisor.se/Restaurants-g189843-Karlskrona_Blekinge_County.html#EATERY_OVERVIEW_BOX'
    
#hämtar url
response = requests.get(url)

#parse av html med beautiful soup
tripadvisor_soup = bs.BeautifulSoup(response.text,features="html.parser")


#hämta ut alla containers som innehåller den text vi vill skrapa
restaurant_containers = tripadvisor_soup.find_all('div', class_ = 'ui_column is-9 shortSellDetails')


#listar alla kategorier på sidan utan att gruppera per container och sparar ner i en lista
kategorier = ([i.text for i in tripadvisor_soup.find_all("a", class_ = "item cuisine")])


#funktion för att hämta ut unika kategorier
def unique(kategorier):
    """funktionen hämtar ut alla unika kategorier"""
    # skapa en tom lista att lagra de unika värdena
    unique_list = [] 
    # itererar igenom alla kategorier och lägger till i den toma listan om de inte redan finns med
    for x in kategorier: 
        if x not in unique_list: 
            unique_list.append(x) 
    #printar ut alla unika värden i vår nya lista och returnerar dem för att sedan kunna spara ner i en variabel
    for x in unique_list: 
        print(x)
    return unique_list    
        
        
unikaKategorier = unique(kategorier)


#räknar antalet förekomster per kategori
antalKategorier = ([kategorier.count(i) for i in unikaKategorier])

#spara ner listor i en dataframe
df_kategorier = DataFrame(
        {"Kategori": unikaKategorier,
         "Antal": antalKategorier})
    
#print(df_kategorier)
                
               
#kod för att plotta datafram i ett horisontellt stapeldiagram
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from math import pi

output_file('MA_Food_Barchart.html')

source = ColumnDataSource(df_kategorier)

sorted_df = df_kategorier.sort_values(by=['Antal'])

p_hmat = figure(y_range=sorted_df['Kategori'], x_range=(0, df_kategorier[['Antal']].values.max() + 1), 
           plot_height=480, plot_width=608, title='Matutbud i Karlskrona', 
           toolbar_location=None, tools='hover', tooltips=('@Antal'))  
  
#horisontella staplar
p_hmat.hbar(y='Kategori', height=0.5, left=0, right='Antal', source=source, color="#c9d9d3")       


p_hmat.y_range.range_padding = 0.1
p_hmat.ygrid.grid_line_color = None
p_hmat.yaxis.axis_label = 'Matutbud'
p_hmat.xaxis.axis_label = 'Antal restauranger'

show(p_hmat)