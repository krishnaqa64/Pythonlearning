import pandas as pd
df=pd.read_csv("data\survey_results_public.csv",index_col="Respondent")
df1=pd.read_csv("data\survey_results_schema.csv",index_col="Column")
print(df.head(2))

#print(df[['ConvertedComp','Country']])

print(df['ConvertedComp'].median())
# print(df.median())
print("\n")

#print(df.describe())
country_grp= df.groupby('Country')

cg=country_grp.get_group("India")
# print(cg["Gender"].value_counts())
#
# #Using filter
# filt=df['Country']=='India'
# print(df.loc[filt,'Gender'].value_counts())
#
#
# print(country_grp['Gender'].value_counts().loc['India'])
#
# print(country_grp['Gender'].value_counts())

print(country_grp['Gender'].value_counts().loc['Afghanistan'])