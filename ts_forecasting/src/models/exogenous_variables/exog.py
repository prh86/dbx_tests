import datetime
import numpy as np
import pandas as pd
from pandas.core.series import Series
from pandas import DataFrame
from functools import partial 


def get_day(
        row: Series,
        date_col : str
    ) -> int:
    """
    Returns the day of the month
    """
    return row[date_col].day

def get_dayofweek(
        row: Series,
        date_col : str
    ) -> int:
    """
    Returns the day of the week
    """
    return row[date_col].dayofweek

def get_month(
        row: Series,
        date_col : str
    ) -> int:
    """
    Returns the month
    """
    return row[date_col].month
