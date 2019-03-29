#import panda
import pandas as pd
import bokeh.sampledata
#bokeh.sampledata.download() - Installed once, then made to comment.
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

df = pd.DataFrame(AAPL)
df['date'] = pd.to_datetime(df['date'])

<<<<<<< HEAD:PythonScript/Py KPI script/KPI_revenueYeat.py
#outputfil för graf KPI_revenueYeat.html
output_file("KPI_revenueYeat.html")
=======
output_file("KPI_revenueYear.html")
>>>>>>> 1c8babde7e2c63f4db7203b8de677d0dc3628433:PythonScript/Py KPI script/KPI_revenueYear.py

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

p.line(df['date'], df['close'], color='navy', alpha=0.5)

p.title.text = 'Försäljning över tid'
p.xaxis.axis_label = 'År'
p.yaxis.axis_label = 'Försäljning i tkr.'


show(p)