import pandas as pd
df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
schema_df=pd.read_csv("data\survey_results_schema.csv",index_col="Column")
df2 = pd.read_csv('data2/data2.csv')


# print(df2)

def func(x):
    if x > 50:
        return "Hot"
    return "normal"


#adding columns
df2["Status"]=df2["Humidity"].apply(func)
print(df2)
print(df2.drop(columns=['Weather',"Wind"]))

