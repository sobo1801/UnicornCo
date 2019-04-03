# UnicornCo
Gruppinlämning för Unicorn Co. - Restaurangbranschen

Market_Analysis_dash.html är masterdokument/dashboard för grafer som relaterar till undersökning av etablering av ny restaurang.
Pythonkod skrivs för varje graf i egen fil med formatet MA_GrafensNamn.py
Output för bokeh-visualisering är MA_GrafensNamn.html
MA_GrafensNamn.html länkas in i Market_Analysis_dash

Unicorn_KPI_dash.html är masterdokument/dashbaord för grafer som relaterar till föreslagna KPIer för den nyetablerade restaurangen.
Pythonkod skrivs för varje graf i egen fil med formatet KPI_GrafensNamn.py
Output för bokeh-visualisering är KPI_grafensNamn.html
KPI_GrafensNamn.html länkas in i Market_Analysis_dash

Style.css innehåller formattering för Market_Analysis_dash.html och Unicorn_KPI_dash.html

#Färgkoder i diagram och dashboard
Blågrön: #5ab4ac
Mörkgrön: #01665e
Ljuslila: #af8dc3
Rosa: #ef8a62
Ljusgrön: #7fbf7b
Mörklila: #762a83
Vniröd: #b2182b

Datakälla i SQL anges i Python-scriptet enligt:

#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7DE79HGT;'
                      'Database=Restaurang;'
                     'Trusted_Connection=yes;')

#sparar ner sql-datan i en panda dataframe
df = pd.read_sql_query('SELECT * FROM restauranger_sales_trend', conn)