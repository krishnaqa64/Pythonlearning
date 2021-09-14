import pandas as pd

df=pd.read_csv("data2/data2.csv",index_col=None)
print(df)
print("\n")
print(df['Weather'].value_counts())
print("\n")

#unique values in a column
print(len(df['Weather'].value_counts()))
print("\n")

#nunique() tells the count of unique values in a column
print(df['Weather'].nunique())
print("\n")

#unique() list of values in a column
print(df['Weather'].unique())
print("\n")
print(df.describe())
print("\n")
print(df.describe().loc[['count','max','mean'],['Temperature','Wind']])

# print(df['Weather'])
# print(df.Weather)

print("\n")
print("Sorting values by column :- ")
df.sort_values(by='Day', inplace=True)
print(df)
print("\n")
#to_datetime()

# print(df)
# df=df['Weather'].drop_duplicates(inplace=True)
# print(df)

#Fill na in a column with values
print("Fill na in a column with values :-")
df.loc[3,'Play']='Yes'
print(df)
df["Play"].fillna("No",inplace=True)
print(df)

print("\n")
print("Shape of dataframe :-")
print(df.shape)
print("random sample of df :- ")
print(df.sample(2))
print("\n")


#data_1['City temp'].fillna(38.5, inplace=True)


