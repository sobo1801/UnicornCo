# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:06:04 2019

@author: sofia
"""


import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, FactorRange
from bokeh.models.tools import HoverTool
from bokeh.core.properties import value
from bokeh.io import show, output_file

  
# read data in dataframe 
df_befolkning = pd.read_csv('Befolkningsdata2018.csv', encoding = 'ISO-8859-1') 
df_befolkning = df_befolkning.sort_values(by='25-64 år', ascending=False)

data = df_befolkning.to_dict(orient='list')
Regions = df_befolkning['Region'].tolist()
categories = df_befolkning.columns.values[2:].tolist()
colors = ['#c9d9d3', '#718dbf', '#e84d60']

source = ColumnDataSource(data)

p = figure(x_range=Regions, plot_height=500, plot_width=800, title='Befolkning per region',
           toolbar_location=None, tools='hover', tooltips='$name : @$name')

p.vbar_stack(categories, x='Region', width=0.9, color=colors, source=source, legend=[['0-24 år'],['25-64 år'],['65+ år']])

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = 'top_right'
p.legend.orientation = 'horizontal'
p.xaxis.major_label_orientation = 3.14/4
p.xaxis.axis_label = 'Region'
p.yaxis.axis_label = 'Befolkning'


output_file('MA_Population_StackedBarChart.html')

show(p)





