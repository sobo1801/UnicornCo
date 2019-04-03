#importera bokehbibliotek
from bokeh.plotting import figure, show, output_file

#outputfil av visualisering i html
output_file('KPI_guestHour.html')

#kod för graf
p = figure(plot_width=400, plot_height=400)
p.vbar(x=[10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00], width=0.5, bottom=0,
       top=[10, 11, 30, 25, 23, 15, 17, 30, 35, 30, 25, 20, 13, 14], color="grey")

#axeltext
p.title.text = 'Besökare per timme'
p.xaxis.axis_label = 'Klockslag'
p.yaxis.axis_label = 'Antal besökare'

#visa plot i fönster
show(p)