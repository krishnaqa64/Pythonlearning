import pandas as pd
df=pd.read_csv("data\survey_results_public.csv")

pd.set_option('display.max_columns',85 )
pd.set_option('display.max_rows',85 )

# print(df.head(5))
# print(df.tail(5))
# print(df.shape)

df2 = pd.read_csv('data2/data2.csv', index_col=['Day'])
#print(df2)
print(df2.head())
# print(df2.tail())

#loc example
# print("\n")
# print(df2.loc[['Tue','Wed'], 'Temperature'])
# print("loc example :-  \n ",df2.loc[["Mon","Wed"],["Weather","Temperature"]])
# print("\n")
#
#iloc example
print("iloc ex1:-  \n ",df2.iloc[0])
print("\n")
print("iloc ex2 :-  \n ",df2.iloc[[0,1],2])
print("\n")
print("iloc ex3 :-  \n ",df2.iloc[[0,1]])
#
# print("\n")
# df=pd.read_csv("data\survey_results_public.csv")
# print(df.loc[0:2,"Hobbyist":"Employment"])
#
