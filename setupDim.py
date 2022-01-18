import time
import pandas as pd
import sqlalchemy
import logging



def create_dimDate(start="2009-01-01", end="2017-12-31"):
    dimDate = pd.DataFrame()
    date_range = pd.date_range(start=start, end=end, freq='1d')
    dimDate['date'] = date_range
    dimDate['year'] = date_range.year
    dimDate['month_no'] = date_range.month
    dimDate['week'] = date_range.isocalendar().week
    dimDate['day_no'] = date_range.day
    dimDate['month'] = date_range.month_name(locale='English')
    dimDate['Weekday'] = date_range.day_name(locale='English')
    dimDate['datekey'] = dimDate.year * 10000 + dimDate.month_no * 100 + dimDate.day_no
    dimDate['datekey'] = dimDate['datekey'].astype(str)
    # dimDate['datekey'] = dimDate.datekey.to_string()


    print(dimDate.columns)
    return dimDate


def writeToDB(tablename, df, if_exists='replace', test=False, pwd=""):
    database = "CrimeTimeDW"
    if test:
        username = 'sa'
        host = 'localhost'
        if pwd == "":
            password = 'Strong password'
    else:
        username = "awdemo"
        host = r"87.92.13.122\DESKTOP-FL66USV,5019"
        if pwd == "":
            password = r"Atlanta2022"

    connection_url = sqlalchemy.engine.URL.create(
        "mssql+pyodbc",
        username=username,
        password=password,
        host=host,
        database="CrimeTimeDW",
        query={
            "driver": "ODBC Driver 17 for SQL Server",
            # "authentication": "ActiveDirectoryIntegrated",
        }
    )
    engine = sqlalchemy.create_engine(connection_url)
    logging.info("connecting host: %s  DB: %s", host, database)
    try:
        df.to_sql(tablename, con=engine, if_exists=if_exists)
    except Exception as e:
        print("error:")
        print(e)
        logging.warning("fail to write to %s", tablename)
    else:
        logging.info("Finished writing to %s", tablename)


if __name__ == "__main__":
    test = False
    logging.basicConfig(
        filename='loading.log',
        encoding='utf-8',
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s")

    dimDate = create_dimDate()
    print(dimDate.dtypes)
    writeToDB('dimDate', dimDate, test=test)
