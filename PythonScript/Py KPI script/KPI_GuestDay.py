#importera pandabibliotek
import pandas as pd
from bokeh.plotting import figure, output_file, show

#output fil i html
output_file("KPI_GuestDay.html")

p = figure(plot_width=500, plot_height=500)

# add a line renderer

p.line([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 
       [15, 9, 11, 11, 9, 25, 30, 15, 5, 9, 100, 10, 12, 13, 20, 20, 15, 12, 18, 20, 20, 13, 4, 5, 6, 7, 8, 2, 7, 20, 36], line_width=2)

#axeltext
p.title.text = 'Antal besökare under en månad'
p.xaxis.axis_label = 'Januari 2018'
p.yaxis.axis_label = 'Antal gäster'


#visa plot i fönster
show(p)

