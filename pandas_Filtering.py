import pandas as pd



df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")


df2 = pd.read_csv('data2/data2.csv')
fil1=(df2["Weather"]=="Sunny")
#print(df2[fil1])
#print(df2)

print(df2.loc[fil1]) #passing series of booleans to loc can also be used to filter df
#print(df2.iloc[[0,1,2,3,4,5,6] ,1])


print("\n")
fil2=((df2["Weather"]=="Sunny" ) & (df2["Temperature"]>15))
print(df2.loc[fil2])
print("\n")
print(df2.loc[~fil2])


print(schema_df.loc['CompTotal',"QuestionText"])

high_sal=df['CompTotal']>100000

print(df.loc[high_sal,"MainBranch":"CompTotal"])
print(df.loc[high_sal,["CompTotal","Country",'LanguageWorkedWith']])

print("\n")
print("\n")


#Filter by columns
cntry=['United States','India', 'United Kingdom', 'Canada']
filter2=df['Country'].isin(cntry)
print(df.loc[filter2,'Country'])


#string filtering
filt=df['LanguageWorkedWith'].str.contains("Python",na=False)
print(df.loc[filt,['LanguageWorkedWith']])
