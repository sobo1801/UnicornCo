#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pyodbc 
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7DE79HGT;'
                      'Database=Restaurang;'
                     'Trusted_Connection=yes;')

#sparar ner sql-datan i en panda dataframe
df = pd.read_sql_query('SELECT * FROM restauranger_sales_trend', conn)

print(df)

#Här skriver du kod för att hantera ditt dataset som är sparat i df

#Här skriver du din Bokeh Api-kod
