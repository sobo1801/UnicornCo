#Import av bokeh-funktioner som används i barchart
import pandas as pd
#import numpy as np TA BORT??
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import dodge
from bokeh.core.properties import value
from math import pi
import openpyxl
import xlrd


#sparar ner sql-datan i en panda dataframe
# Måste ange columnnamnen att läsa in i det fall de innehåller siffror.
df = pd.read_excel('Data\RestaurantRevenue_data.xlsx', names = ['Kategori', '2017', '2018'])      

output_file("MA_Restaurant_BarChart.html")

# data = df.to_dict(orient='list') TA BORT???
# print(data) TA BORT??

idx = df['Kategori'].tolist()
#print(idx)

source = ColumnDataSource(df)


p = figure(x_range=idx, y_range=(0, df[['2017', '2018']].values.max() + 5), 
           plot_height=480, title="Sales per category and year", 
           toolbar_location=None, tools="")


p.vbar(x=dodge('Kategori', -0.12, range=p.x_range), top='2017', width=0.2, source=source,
       color="#c9d9d3", legend=value("2017"))

p.vbar(x=dodge('Kategori',  0.12,  range=p.x_range), top='2018', width=0.2, source=source,
       color="#718dbf", legend=value("2018"))


p.x_range.range_padding = 0.2
p.xgrid.grid_line_color = None
p.legend.location = 'top_left'
p.legend.orientation = 'horizontal'
p.xaxis.major_label_orientation = pi/4

show(p)
