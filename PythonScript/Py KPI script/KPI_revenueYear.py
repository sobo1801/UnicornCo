#import panda
import pandas as pd
import bokeh.sampledata
#bokeh.sampledata.download() - Installed once, then made to comment.
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

df = pd.DataFrame(AAPL)
df['date'] = pd.to_datetime(df['date'])

output_file("KPI_revenueYear.html")

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

p.line(df['date'], df['close'], color='navy', alpha=0.5)

p.title.text = 'Försäljning över tid'
p.xaxis.axis_label = 'År'
p.yaxis.axis_label = 'Försäljning i tkr.'


show(p)