import numpy as np
import pandas as pd
df=pd.read_csv("data2/data2.csv",index_col=None)




df['Conditions']=df['Weather'].apply(lambda x:"playable" if x=="Sunny" else "Cannot Play")
print(df)

def func1(x):
    if x=="Sunny": return "Play"
    elif x=="Cloudy": return "Doubtful"
    else : return "Cannot play"

df['Conditions']=df['Weather'].apply(func1)
print(df)



df.loc['Averages','Temperature']=df["Temperature"].mean()
df.loc['Averages','Wind']=df["Wind"].mean()
df.loc['Averages','Humidity']=df["Humidity"].mean()
df.loc['Averages']=df.loc['Averages'].replace(np.NAN,"Not valid")

print(df)