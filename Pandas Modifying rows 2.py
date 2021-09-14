import pandas as pd
df=pd.read_csv("data2/data2.csv",index_col=None)



# df['Day'][6]="Holiday"
print(df)
print("\n")
print(df['Weather'][6])

filt3=df["Day"]=="Sun"

print("\n")
df.loc[filt3,'Weather']="Shower"
print(df[filt3]['Weather'])
print(df.loc[filt3,'Weather'])
print("\n")
print("*****************************************")
print(df)
#print(type(df.loc[filt3,'Weather']))
print("\n")
df['Weather'][6]="Sunny"
print(df)
df[filt3]['Weather']="Cloudy"
print(df)
df.loc[filt3,'Weather']="Cloudy"
print(df)


filt3=df["Weather"]=='Shower'
df.loc[filt3,"Playable"]="No"


# filt1=df["Weather"]=='Sunny'
# filt2=df["Weather"]=='Cloudy'
# df.loc[filt1,'Play']='Yes'
# df.loc[filt2,'Play']='Maybe'
print(df)
df['Playable'].fillna("Yes",inplace=True)
print(df)

for x in range(7):
    df.loc[x,'Days']="Holiday{y}".format(y=x)

print(df)

