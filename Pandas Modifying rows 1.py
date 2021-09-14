import pandas as pd
df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")
df2 = pd.read_csv('data2/data2.csv')


print(df2.loc[[1,2],"Day":"Wind"])

df2.iloc[1,2]=19.37
print(df2.loc[[1,2],"Day":"Wind"])

print("\n")
print(df2.iloc[2,[2,3]] )
df2.iloc[ 2,[2,3]] =[18.32,18]
#
# print(df2)


filt3=df2["Day"]=="Sun"

print(df2[filt3]['Weather'])
df2[filt3]['Weather']="Shower" # incoorect assignment (dont do it here instead use iloc)
print("\n")
print('********************')
print("\n")
df2.loc[filt3,'Weather']="Shower" # instead use loc
print(df2)

#df2.loc[fil1]['Weather'] = 'Showers'  #incorrect assignment
#print(df2)

print("\n")
print('********#apply , map , applymap , replace ************')
print("\n")

#apply , map , applymap , replace
#applying value to full series

print("length :-\n", df2['Weather'].apply(len))
print("lenghtxx :-",len(df2['Weather']))
print("\n")
# print(df2.len())
print(df2.apply(len))

print("\n")
print("axis len : \n ", df2.apply( len,axis='columns'))


def up(x):
    return x.upper()

df2['Weather']=df2["Weather"].apply(up)
print(df2)

df2['Weather']=df2["Weather"].apply(lambda x:x.lower())
print(df2)

print("\n")
print(df2.apply(pd.Series.min))

print(df2.apply(lambda x:x.min()))

# running apply on series applies function to every values in series
# running apply on dataframe applies function to every series  in df
#running apply map on dataframe applies function to every value in df

#print(df2.applymap(len))

print(df2)
df2['Weather'].replace({'sunny':"Sunny", 'shower':"Shower"},inplace=True)
print(df2)

filt4=df2['Weather']=='Sunny' #filter based on row values
print(df2.loc[filt4])
print(df2.loc[filt4,"Weather"])
df2.loc[filt4,"Weather"]="Radiant"
print(df2)


print(df2.apply(pd.Series.min))
print(df2.apply(lambda x:x.min()))
print("\n")
print(type(df2['Temperature']))
print(df2['Temperature'].min())

#map function only works on series , it can be used to substitute each value in series with another value

print(df2['Day'].map({'Mon':"Monday"}))  # map replaced values we didnt map to NAN values , so instead replace
print(df2['Day'].replace({'Mon':"Monday"}))