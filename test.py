import pandas as pd

df=pd.read_csv("data2/data2.csv",index_col=None)
# print(df.head(1))
print("\n")
#print(df.loc[0:2,'Day':'Temperature'])
#print(df.loc[[0,3],'Day':'Temperature'])
#
# fil1=df['Weather']=="Shower"
#
# print(df.loc[fil1]['Weather'])
# print(df.loc[fil1,'Weather'])
#
# df.loc[fil1]['Weather'] = 'Showers'
# print(df)
# df.loc[fil1,'Weather'] = 'Showers'
print(df)
print(df['Day'])

# for x in range(7):
#     df.loc[x,'Day']="Holiday{y}".format(y=x)

for x in range(7):
    df.loc[x,'Days']="Holiday{y}".format(y=x)

print(df)

df.loc[0,'Play']='Yes'
print(df)

