import pandas as pd

df=pd.read_csv("data\survey_results_public.csv")

pd.set_option('display.max_columns',85 )
pd.set_option('display.max_rows',85 )

print(df.head(5))
print(df.tail(5))
print("rows and columns count :- " ,df.shape)

print(df.columns)

print(df["Hobbyist"].head(3))
print("\n")
print(df["Hobbyist"].value_counts())  #unique values in the column with counts
print("\n")
print(df["Country"].value_counts())
