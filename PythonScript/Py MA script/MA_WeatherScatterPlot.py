#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter
from bokeh.models.tools import HoverTool
from bokeh.transform import transform, factor_cmap


#sparar ner sql-datan i en panda dataframe
df_weahter = pd.read_excel('Weather_data.xlsx')

output_file('geografisk_plats.html')

print(df_weahter)

#Här skriver du kod för att hantera ditt dataset som är sparat i df

#Här skriver du din Bokeh Api-kod

source = ColumnDataSource(df_weahter)

#Val av färg till plotten
colors = ["#4575b4", "#91bfdb", "#e0f3f8", "#fee090", "#fc8d59", "#d73027"]

#Anger att cirklarna ska färgsättas utifrån temperaturen i aktuell stad.
mapper = LinearColorMapper(palette=colors, low=df_weahter.Temepratur_avg.min(), high=df_weahter.Temepratur_avg.max())

p = figure(toolbar_location="above")
p.circle(x='Solskenssekunder_avg', y='Vindhastighet_avg',
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

hover = HoverTool()
hover.tooltips=[
    ('Station: ', '@Station'),
    ('Medelvind: ', '@Vindhastighet_avg{(0.0)}'),
    ('Soltid: ', '@Solskenssekunder_avg{(0,0)}'),
    ('Temperatur: ', '@Temepratur_avg{(00.0 a)}')
]


p.add_tools(hover)

show(p)
