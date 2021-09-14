import pandas as pd

df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")
df2 = pd.read_csv('data2/data2.csv')

print(df2.columns)

#updating Column names
df2.columns =[x.upper() for x in df2.columns]
print(df2.columns)

#replace blanks in column names
df2.columns= df2.columns.str.replace(" ",'_')

#rename Columns
df2.rename(columns={'DAY': "CurrentDayOfWeek"},inplace=True)
print(df2.columns)


