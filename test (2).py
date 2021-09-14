import pandas as pd

df=pd.read_csv("data2/data2.csv",index_col=None)


df['Condition']=df['Weather'].apply(lambda x:"Play" if x=="Sunny"   else "Dont play")

df['Condition'].replace({'Dont play': "Bad weather"},inplace=True)
print(df)

#print(df.loc[6].unique())
#print(df.describe())

def func1(x):
    if x=="Cloudy":
        return "Play"


filt=df["Weather"]=='Cloudy'
df.loc[filt,"Condition"]='Play'

#df['Condition']=df["Weather"].apply(func1)
print(df)

filt2=df["Weather"]=='Shower'
df.loc[filt2,"Condition"]='Cannot Play'
print(df)