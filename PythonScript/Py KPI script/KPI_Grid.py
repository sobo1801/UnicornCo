#importera pandabibliotek och bokeh
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot, layout
from bokeh.models import Toggle, BoxAnnotation, CustomJS
from bokeh.models.glyphs import Text
import bokeh.sampledata
# bokeh.sampledata.download() - Installed once, then made to comment.
from bokeh.sampledata.stocks import AAPL


###Graf för att visa gäster per dag
p_dag = figure(plot_width=400, plot_height=400)

# add a line renderer
p_dag.line([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 
       [15, 9, 11, 11, 9, 25, 30, 15, 5, 9, 100, 10, 12, 13, 20, 20, 15, 12, 18, 20, 20, 13, 4, 5, 6, 7, 8, 2, 7, 20, 36], 
       line_width=2, color='#762a83')

#axeltext
p_dag.title.text = 'Antal besökare under en månad'
p_dag.xaxis.axis_label = 'Januari 2018'
p_dag.yaxis.axis_label = 'Antal gäster'


####Graf för att visa gäster per timme
#kod för graf
p_timme = figure(plot_width=400, plot_height=400)
p_timme.vbar(x=[10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00], width=0.5, bottom=0,
       top=[10, 11, 30, 25, 23, 15, 17, 30, 35, 30, 25, 20, 13, 14], color='#5ab4ac')

#axeltext
p_timme.title.text = 'Besökare per timme'
p_timme.xaxis.axis_label = 'Klockslag'
p_timme.yaxis.axis_label = 'Antal besökare'



####Graf för att visa menysättning
#kod för att skapa graf
p_meny = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p_meny.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

p_meny.xgrid.bounds = (3, 3.001)
p_meny.ygrid.bounds = (4.5, 4.501)

p_meny.title.text = 'Lönsamhet vs Popularietet'
p_meny.xaxis.axis_label = 'Lönsamhet'
p_meny.yaxis.axis_label = 'Popularitet'


#labels
#Bottom-left box
box = BoxAnnotation(left=0, right=3, bottom=0, top=4.5 ,fill_color='#5ab4ac', fill_alpha=0.1)
p_meny.add_layout(box)
#Bottom-right box
box = BoxAnnotation(left=3, right=6, bottom=0, top=4.5 ,fill_color='#af8dc3', fill_alpha=0.1)
p_meny.add_layout(box)
#Top-left box
box = BoxAnnotation(left=0, right=3, bottom=4.5, top=8 ,fill_color='#ef8a62', fill_alpha=0.1)
p_meny.add_layout(box)
#Top-right box
box = BoxAnnotation(left=3, right=6, bottom=4.5, top=8 ,fill_color='#7fbf7b', fill_alpha=0.1)
p_meny.add_layout(box)

#Bottom-left text
p_meny.text(x=["2", "3"], y=["3", "3"], text=["Byrackor"],text_align="center", text_baseline="middle")
#Bottom-right text
p_meny.text(x=["4", "3"], y=["3", "3"], text=["Frågetecken"], text_align="center", text_baseline="middle")
#Top-left box text
p_meny.text(x=["2", "6"], y=["6", "3"], text=["Kassakor"], text_align="center", text_baseline="middle")
#Top-right box text
p_meny.text(x=["4", "6"], y=["6", "6"], text=["Stjärnor"], text_align="center", text_baseline="middle")


####Graf för att visa gäster per omsättning
#data sparas i panda dataframe
df = pd.DataFrame(AAPL)
df['date'] = pd.to_datetime(df['date'])

# create a new plot with a datetime axis type
p_omsättning = figure(plot_width=1200, plot_height=370, x_axis_type="datetime")

p_omsättning.line(df['date'], df['close'], color='#762a83', alpha=0.5)

#titeltext
p_omsättning.title.text = 'Försäljning över tid'
p_omsättning.xaxis.axis_label = 'År'
p_omsättning.yaxis.axis_label = 'Försäljning i tkr.'


# make a grid

output_file("KPI_Grid.html")
grid = gridplot([[p_dag, p_timme, p_meny], [p_omsättning]])

# show the results
show(grid)