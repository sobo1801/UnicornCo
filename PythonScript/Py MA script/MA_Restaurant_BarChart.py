#Import av bokeh-funktioner och panda
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import dodge
from bokeh.core.properties import value
from math import pi
import openpyxl
import xlrd


#läser in exceldata i en panda dataframe. Nödvändigt att ange kolumnnamn då de innehåller siffror
df = pd.read_excel('Data\RestaurantRevenue_data.xlsx', names = ['Kategori', '2017', '2018'])      

#outputfil för visualisering i HTML
output_file("MA_Restaurant_BarChart.html")

#sätter index
idx = df['Kategori'].tolist()

source = ColumnDataSource(df)

#bokeh graf kod
p = figure(x_range=idx, y_range=(0, df[['2017', '2018']].values.max() + 5), 
           plot_height=480, title='Omsättning per kategori och år', 
           toolbar_location=None, tools="")

#kod för indivuduella staplar
p.vbar(x=dodge('Kategori', -0.12, range=p.x_range), top='2017', width=0.2, source=source,
       color="#c9d9d3", legend=value("2017"))

p.vbar(x=dodge('Kategori',  0.12,  range=p.x_range), top='2018', width=0.2, source=source,
       color="#718dbf", legend=value("2018"))


p.x_range.range_padding = 0.2
p.xgrid.grid_line_color = None
p.legend.location = 'top_right'
p.legend.orientation = 'horizontal'
p.xaxis.major_label_orientation = pi/4
p.xaxis.axis_label = 'Kategori'
p.yaxis.axis_label = 'Omsättning mSEK'


#visa graf i fönster
show(p)
