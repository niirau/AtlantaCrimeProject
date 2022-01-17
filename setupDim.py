import time
import pandas as pd
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
    # dimDate['datekey'] = dimDate.datekey.to_string()

    print(dimDate.columns)
    return dimDate


def writeToDB(tablename, overwrite='replace', test=False):
    pass


if __name__ == "__main__":
    test = False

    print(create_dimDate())

    logging.basicConfig(
        filename='loading.log',
        encoding='utf-8',
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s")

    if test:
        host = 'localhost'
        password = 'Strong password'
    else:
        host = "87.92.13.122\DESKTOP-FL66USV,1433"
        password = "Password1"
