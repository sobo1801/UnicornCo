#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, FactorRange
from bokeh.models.tools import HoverTool
from bokeh.transform import transform, factor_cmap
from bokeh.palettes import Spectral11


#sparar ner sql-datan i en panda dataframe
#url = 'https://github.com/sobo1801/UnicornCo/blob/master/Data/RestaurantTrend_data.xlsx'
df = pd.read_excel('RestaurantTrend_data.xlsx')

output_file("MA_MarkettrendLineChart.html")

#print(df)

#Här skriver du kod för att hantera ditt dataset som är sparat i df

#Här skriver du din Bokeh Api-kod
p = figure(plot_width=600, plot_height=400, x_range=df['År'], title = 'Mattrender, procentuell förändring',
           toolbar_location="above")

p.line(df['År'], df['Hotellrestauranger'], color='#a6cee3', alpha=0.8, line_width=3, legend = ('Hotellrestauranger'))
p.line(df['År'], df['Caféer'], color='#1f78b4', alpha=0.8, line_width=3, legend = ('Caféer'))
p.line(df['År'], df['Snabbmatsrestauranger'], color='#b2df8a', alpha=0.8, line_width=3, legend = ('Snabbmatsrestauranger'))
p.line(df['År'], df['Lunch- och kvällsrestauranger'], color='#33a02c', alpha=0.8, line_width=3, legend = ('Lunch- och kvällsrestauranger'))
p.line(df['År'], df['Nöjesrestauranger'], color='#fb9a99', alpha=0.8, line_width=3, legend = ('Nöjesrestauranger'))
p.line(df['År'], df['Trafiknära restauranger'], color='#984ea3', alpha=0.8, line_width=3, legend = ('Trafiknära restauranger'))
p.line(df['År'], df['Personalrestauranger'], color='#fdbf6f', alpha=0.8, line_width=3, legend = ('Personalrestauranger'))


hover = HoverTool()
hover.tooltips=[
    ('Kategori: ', ''),
    ('Värde: ', '@value')
]
p.add_tools(hover)


p.xgrid.grid_line_color = None
p.legend.location = 'bottom_left'
p.legend.orientation = "vertical"
p.legend.label_text_font_size = '8pt'
p.legend.spacing = 0
#Möjliggör att välja bort vissa kategorier och bara visa de vi vill
p.legend.click_policy="hide"

show(p)
