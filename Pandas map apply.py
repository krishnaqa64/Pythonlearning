#https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff

import pandas as pd
import numpy as np
df = pd.DataFrame({ 'A': [1,2,3,4],
                   'B': [10,20,30,40],
                   'C': [20,40,60,80]
                  },
                  index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])




#applying map on dataframe
print("\n apply() on Dataframe :- ")
print(df)
def custom_sum(row):
    #print(row) #full row gets passed to function , as it is applied on dataframe
    return row.sum()

df['D'] = df.apply(custom_sum, axis=1)
print(df)

df.loc['Row 5'] = df.apply(custom_sum, axis=0)
print(df)




def cal_multi_col(row):
    return [row['A'] * 2, row['B'] * 3]








#applying on series

print("\n apply() on Series :- ")

def multiply_by_2(val):
    #print(type(val))   # passes one value of series at a time)
    #print(val)
    #rint("\n")
    return val * 2
df['E'] = df['D'].apply(multiply_by_2)
print(df)

#lambda apply function
#df['A']=df['A'].apply(lambda x:x*x if x%2==0 else x+x)



print("\n APPLY MAP :- ")
#applymap() is only available in DataFrame and used for element-wise operation across the whole DataFrame.

df=df.applymap(np.square)
print(df)


#How to use map()?
#map() is only available in Series and used for substituting each value in a Series with another value. To understand how the map() works, we first create a Series.
df2 = pd.read_csv('data2/data2.csv')
print(df2['Day'].map({'Mon':"Monday"}))  # map replaced values we didnt map to NAN values , so instead replace
print(df2['Day'].replace({'Mon':"Monday"}))