import pandas as pd
import requests
import sqlalchemy
import logging
import pyodbc

test = True

logging.basicConfig(
    filename='loading.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s")
logging.info("started new import, test = %s", test)

if test:
    host = 'localhost'
    password = 'Strong password'
else:
    host = "87.92.13.122\DESKTOP-FL66USV,1433"
    password = "Password1"

url = "https://datausa.io/api/data?measure=Household%20Income%20by%20Race,Household%20Income%20by%20Race%20Moe&drilldowns=Race&Geography=16000US1304000:parents,16000US1304000,16000US1304000:similar"
r = requests.get(url)

connection_url = sqlalchemy.engine.URL.create(
    "mssql+pyodbc",
    username="sa",
    password=password,
    host=host,
    database="CrimeTimeDW",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        # "authentication": "ActiveDirectoryIntegrated",
    }
)
engine = sqlalchemy.create_engine(connection_url)
logging.debug("connection status code: %s", r.status_code)

# crime = pd.read_csv('datasets/atlcrime.csv')


text = eval(r.text)
pop = pd.DataFrame(text['data'])
try:
    pop.to_sql('pop', con=engine, if_exists="replace")
except Exception as e:
    print("error:")
    print(e)
    logging.warning("fail to write to pop")
else:
    print("wrote to pop")
    logging.info("Finished writing to pop")
"""
try:
    crime.to_sql('crime', con=engine, if_exists="replace", method='multi')
except Exception as e:
    print("error:")
    print(e)
    logging.warning("fail to write to crime")
else:
    print("wrote to crime")
    logging.info("Finished writing to crime")
"""
