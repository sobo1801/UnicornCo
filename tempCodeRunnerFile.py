#Import av Python ODBC och Panda dataframe(tabeller i Python)
import pyodbc 
import pandas as pd

# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:LAPTOP-7DE79HGT.Restaurang.windows.net' 
database = 'Restaurang' 
username = 'gruppen' 
password = 'gruppen' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#sparar ner sql-datan i en panda dataframe
df = pd.read_sql_query('SELECT * FROM restauranger_sales_trend', conn)

print(df)

#Här skriver du kod för att hantera ditt dataset som är sparat i df

#Här skriver du din Bokeh Api-kod