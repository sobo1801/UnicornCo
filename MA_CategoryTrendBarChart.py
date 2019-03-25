#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pyodbc 
import pandas as pd
#import av bokeh-funktioner som används i barchart
from bokeh.io import show, output_file, save
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7DE79HGT;'
                      'Database=Restaurang;'
                     'Trusted_Connection=yes;')

#sparar ner sql-datan i en panda dataframe
df = pd.read_sql_query('SELECT * FROM restauranger_sales_trend', conn)

#print(df)

category = df[["category"]]
sales = df[["total_sales"]]
year = df[["year"]]

#detta är min html-fil som ska innehålla visualiseringen, sparas i projektmappen
output_file("MA_CategoryTrendBarChart.html")

"""category = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']"""

data = df

palette = ["#c9d9d3", "#718dbf", "#e84d60"]

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
"""x = [ (category, year) for category in data for years in year ]
counts = sum(zip(data['2017'], data['2018']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))"""

p = figure(x_range=FactorRange(*x), plot_height=350, title="Fruit Counts by Year",
           toolbar_location=None, tools="")

p.vbar(x="sales", top='category', width=0.9, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=year, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

save(p)

##skapa tabell som visar omsättningstappet år för år per kategori
