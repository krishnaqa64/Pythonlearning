import pandas as pd
df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
print(df.head(2))
schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")
df2 = pd.read_csv('data2/data2.csv')


print(df2.sort_values(by="Temperature"))
print(df2.sort_values(by="Temperature",ascending=False))
#mutiple columns sort
print(df2.sort_values(by=["Temperature","Wind"],ascending=False))

print(df2.sort_values(by=["Temperature","Wind"],ascending=[False,True],inplace=True))


print(df2.sort_index())

print(df2["Temperature"].sort_values())

