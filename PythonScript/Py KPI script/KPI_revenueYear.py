#importera panda och bokeh
import pandas as pd
import bokeh.sampledata
#bokeh.sampledata.download() - Installed once, then made to comment.
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

#data sparas i panda dataframe
df = pd.DataFrame(AAPL)
df['date'] = pd.to_datetime(df['date'])

#output fil i html för grafen
output_file("KPI_revenueYear.html")

# create a new plot with a datetime axis type
p = figure(plot_width=1300, plot_height=370, x_axis_type="datetime")

p.line(df['date'], df['close'], color='navy', alpha=0.5)

#titeltext
p.title.text = 'Försäljning över tid'
p.xaxis.axis_label = 'År'
p.yaxis.axis_label = 'Försäljning i tkr.'

#visa plot i fönster
show(p)