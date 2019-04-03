#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, FactorRange
from bokeh.models.tools import HoverTool
from bokeh.transform import transform, factor_cmap
#from bokeh.palettes import Spectral11
import xlrd


#sparar ner sql-datan i en panda dataframe
df = pd.read_excel('Data\RestaurantTrend_data.xlsx')

output_file("MA_MarkettrendLineChart.html")

#Går ej att läsa in årtalen som en x_range i figuren så därav omvandlar vi dem till en lista först.
df['År'] = list(map(str, df['År']))

#print(df)

#Här skriver du kod för att hantera ditt dataset som är sparat i df

#Här skriver du din Bokeh Api-kod
p = figure(x_range=df['År'], plot_height=480 , title = 'Restaurangtrender, procentuell förändring per år',
           toolbar_location="above")


p.line(df['År'], df['Hotellrestauranger'], color='#5ab4ac', alpha=0.8, line_width=3, legend = ('Hotellrestauranger'))
p.line(df['År'], df['Caféer'], color='#01665e', alpha=0.8, line_width=3, legend = ('Caféer'))
p.line(df['År'], df['Snabbmatsrestauranger'], color='#af8dc3', alpha=0.8, line_width=3, legend = ('Snabbmatsrestauranger'))
p.line(df['År'], df['Lunch- och kvällsrestauranger'], color='#ef8a62', alpha=0.8, line_width=3, legend = ('Lunch- och kvällsrestauranger'))
p.line(df['År'], df['Nöjesrestauranger'], color='#7fbf7b', alpha=0.8, line_width=3, legend = ('Nöjesrestauranger'))
p.line(df['År'], df['Trafiknära restauranger'], color='#762a83', alpha=0.8, line_width=3, legend = ('Trafiknära restauranger'))
p.line(df['År'], df['Personalrestauranger'], color='#b2182b', alpha=0.8, line_width=3, legend = ('Personalrestauranger'))



p.xgrid.grid_line_color = None

#Placering av kategoribeskrivningen:
p.legend.location = 'bottom_left'
p.legend.orientation = "vertical"
p.legend.label_text_font_size = '8pt'
p.legend.spacing = 0
p.xaxis.axis_label = 'År'
p.yaxis.axis_label = 'Procent'

#Möjliggör att välja bort vissa kategorier och bara visa de vi vill
p.legend.click_policy="hide"

show(p)
