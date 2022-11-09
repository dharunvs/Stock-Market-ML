import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader as web

from sklearn.preprocessing import MinMaxScaler  

company = 'TSLA'

start = dt.datetime(2012, 1, 1)
end = dt.datetime(2022, 1, 1)

data = web.DataReader(company, 'yahoo', start, end)
scaler = MinMaxScaler(feature_range=(0, 1))

scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

print(data)
print(scaled_data)