# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:37:56 2019

@author: fatim
"""

#Import av Python ODBC och Panda dataframe(tabeller i Python)


#import av bokeh-funktioner som används i barchart
import pandas as pd
import pyodbc
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, FactorRange
from bokeh.models.tools import HoverTool
from bokeh.transform import transform, factor_cmap
from bokeh.palettes import Spectral11
from bokeh.transform import dodge
from bokeh.core.properties import value
from math import pi

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7DE79HGT;'
                      'Database=Restaurang;'
                     'Trusted_Connection=yes;')

#sparar ner sql-datan i en panda dataframe
df = pd.read_sql_query("""select F1 as Kategori, [2017] as År2017, [2018] as År2018
from utveckling""", conn)
                     

output_file("MA_Restaurant_BarChart.html")

data = df.to_dict(orient='list')
print(data)

idx = df['Kategori'].tolist()
print(idx)

source = ColumnDataSource(data=data)


p = figure(x_range=idx, y_range=(0, df[['År2017', 'År2018']].values.max() + 5), 
           plot_height=250, title="Sales per category and year", 
           toolbar_location=None, tools="")


p.vbar(x=dodge('Kategori', -0.25, range=p.x_range), top='År2017', width=0.2, source=source,
       color="#c9d9d3", legend=value("År2017"))

p.vbar(x=dodge('Kategori',  0.0,  range=p.x_range), top='År2018', width=0.2, source=source,
       color="#718dbf", legend=value("År2018"))


#p.x_range.range_padding = 0.2
p.xgrid.grid_line_color = None
p.legend.location = 'top_left'
p.legend.orientation = 'horizontal'
p.xaxis.major_label_orientation = pi/4

show(p)