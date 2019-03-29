
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import layout
from bokeh.models import Toggle, BoxAnnotation, CustomJS
from bokeh.models.glyphs import Text



# output to static HTML file
output_file("KPI_menuEngineering.html")

p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

#p.xgrid.grid_line_color = None
#p.ygrid.grid_line_color = None
p.xgrid.bounds = (3, 3.001)
p.ygrid.bounds = (4.5, 4.501)

p.title.text = 'Lönsamhet vs Popularietet'
p.xaxis.axis_label = 'Lönsamhet'
p.yaxis.axis_label = 'Popularitet'


#labels
#Bottom-left box
box = BoxAnnotation(left=0, right=3, bottom=0, top=4.5 ,fill_color='green', fill_alpha=0.1)
p.add_layout(box)
#Bottom-right box
box = BoxAnnotation(left=3, right=6, bottom=0, top=4.5 ,fill_color='blue', fill_alpha=0.1)
p.add_layout(box)
#Top-left box
box = BoxAnnotation(left=0, right=3, bottom=4.5, top=8 ,fill_color='yellow', fill_alpha=0.1)
p.add_layout(box)
#Top-right box
box = BoxAnnotation(left=3, right=6, bottom=4.5, top=8 ,fill_color='red', fill_alpha=0.1)
p.add_layout(box)

#Bottom-left text
p.text(x=["2", "3"], y=["3", "3"], text=["Byrackor"], text_color="blue",text_align="center", text_baseline="middle")
#Bottom-right text
p.text(x=["4", "3"], y=["3", "3"], text=["Frågetecken"], text_color="Blue",text_align="center", text_baseline="middle")
#Top-left box text
p.text(x=["2", "6"], y=["6", "3"], text=["Kassakor"], text_color="Blue",text_align="center", text_baseline="middle")
#Top-right box text
p.text(x=["4", "6"], y=["6", "6"], text=["Stjärnor"], text_color="Blue",text_align="center", text_baseline="middle")


# show the results
show(p)