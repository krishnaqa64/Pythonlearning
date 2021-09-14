import pandas as pd

df2 = pd.read_csv('data2/data2.csv')

df2.set_index("Day",inplace=True)  #inplace=True will make changes to original df

print(df2)
print("\n")
print(df2.loc["Mon","Temperature"])
df2.reset_index("Day",inplace=True)  #reset_index will reset the index
print(df2)





df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")

print(df.head(2))

schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")

print(schema_df)
print(schema_df.loc["Hobbyist"])
print(schema_df.loc["MiscTechDesireNextYear",'QuestionText'])


print(schema_df.sort_index())
print(schema_df.sort_index(ascending=False))