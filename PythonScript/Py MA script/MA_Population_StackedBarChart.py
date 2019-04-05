#importera panda och bokeh

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, NumeralTickFormatter
  

# läs in data i panda dataframe 
df_befolkning = pd.read_csv('UnicornCo\Data\Befolkningsdata2018.csv', encoding = 'ISO-8859-1') 

#sortera i storleksordning
df_befolkning = df_befolkning.sort_values(by='25-64 år', ascending=False)

#filtrera ut de regioner som innehåller våra toppstationer Nordkoster, Visby, Öland, Hoburgen, Karlskrona 
region_filter = ['Gotlands län', 'Västra Götalands län', 'Kalmar län', 'Blekinge län']
utvalda_regioner = df_befolkning[df_befolkning['Region'].isin(region_filter)]

#hämta ut data från dataframe i listor för data, regioner och kategorier
data = df_befolkning.to_dict(orient='list')
Regions = utvalda_regioner['Region'].tolist()
categories = df_befolkning.columns.values[2:].tolist()
colors = ['#c9d9d3', '#718dbf', '#01665e']

source = ColumnDataSource(data)


#skapa bokehplot
p = figure(x_range=Regions, plot_height=480, title='Befolkning 2018 per region',
           toolbar_location=None, tools='hover', tooltips='$name : @$name{(0,0)}')

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
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")


#outputfil i HTML för bokehgraf
output_file('MA_Population_StackedBarChart.html')

#visa bokehgraf i fönster
show(p)





