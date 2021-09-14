# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

import pandas as pd
import numpy as np
from datetime import datetime as d

#df=pd.read_csv("data2\ETH_1.csv")

#print(df.head(3))

#df['Date']=pd.to_datetime(df["Date"],format='%Y-%m-%d %I-%p')
#print(df.loc[0, 'Date'].day_name())
#print(df.dtypes)


d_parser = lambda x: d.strptime(x, '%Y-%m-%d %I-%p')
df=pd.read_csv("data2\ETH_1.csv", parse_dates=['Date'], date_parser=d_parser)


# def fun(x):
#     return x.day_name()
# df['Day']=df['Date'].apply(fun)

print(df['Date'].dt.day_name())
print("\n")
print(df['Date'].min())
print("\n")
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2019-01-02'))
#print((df.loc[filt]).shape)
print(df.loc[filt])

print("2019 data :- \n")
df.set_index('Date', inplace=True)
print(df.loc['2019'])

print(df['2020-01':'2020-02'])