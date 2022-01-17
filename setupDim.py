import time
import pandas as pd


def create_dimDate(start="2009-01-01", end="2017-12-31"):
    date_range['date'] = pd.date_range(start=start, end=end, freq='1d')
    date_range['year'] = date_range['date'].year()
    return date_range


if __name__ == "__main__":
    print(create_dimDate())
