# tabular data manipulation
import numpy as np
import pandas as pd
# datetime utilities
from datetime import timedelta, datetime







def formatting(df):
    # converting sale_date to datetime format using to_datetime()
    df.sale_date = pd.to_datetime(df.sale_date)
    # this gives you a df resetting the index to date which has to
    df = df.set_index('sale_date').sort_index()
    # adding a month column
    df['month'] = df.index.strftime('%B')
    # adding a day of the week column
    df['day'] = df.index.strftime('%w')
    return df