
import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people,index=[1,2,3,4,5,6,7])
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)

print(df)
print("\n")
print(df.dropna())
print("\n")
#print(df.dropna(axis="index",how='any'))  # default arguments :- axis="index",how='any'

print(df.dropna(axis="index",how='any'))

print(df.dropna(axis="index",how='all'))
print("\n")
print(df.dropna(axis="columns",how='all'))
print(df.dropna(axis="columns",how='any'))
print("\n")
print(df.dropna(axis="index",how='any',subset=['email']))

print(df.isna())