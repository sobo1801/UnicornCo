#Import av bokeh och Panda dataframe
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter
from bokeh.models.tools import HoverTool
from bokeh.transform import transform, factor_cmap


#sparar ner excel-datan i en panda dataframe
df_weahter = pd.read_excel('Data\Weather_data.xlsx')

#output fil för visualisering i HTML
output_file('MA_WeatherScatterPlot.html')

source = ColumnDataSource(df_weahter)

#Bokehkod för graf

#Val av färg till plotten
colors = ["#0571b0", "#92c5de", "#f7f7f7", "#f4a582", "#ca0020"]

#Anger att cirklarna ska färgsättas utifrån temperaturen i aktuell stad.
mapper = LinearColorMapper(palette=colors, low=df_weahter.Temepratur_avg.min(), high=df_weahter.Temepratur_avg.max())

p = figure(toolbar_location="above", plot_height=480 )
p.circle(x='Solskensminuter_avg', y='Vindhastighet_avg',
         source=source,
         size=10,
         fill_color=transform('Temepratur_avg', mapper))

color_bar = ColorBar(color_mapper=mapper, location=(0, 0),
                     title = 'Genomsnittling Temperatur',
                     ticker=BasicTicker(desired_num_ticks=len(colors)))

p.add_layout(color_bar, 'right')

p.title.text = 'Geografisk data'
p.xaxis.axis_label = 'Genomsnittlig soltid, sek'
p.yaxis.axis_label = 'Genomsnittlig vindhastighet, ms'

#kod för att skapa ett hovertool
hover = HoverTool()
hover.tooltips=[
    ('Station: ', '@Station'),
    ('Medelvind: ', '@Vindhastighet_avg{(0.0)}'),
    ('Soltid: ', '@Solskensminuter_avg{(0,0)}'),
    ('Temperatur: ', '@Temepratur_avg{(00.0 a)}')
]


p.add_tools(hover)

#visa graf i fönster
show(p)
