import pandas as pd

exampledict = {'EmpId' : ['E01','E02','E03','E04'],
       'EmpName' : ['Raj','Atul','Reena','Ayushi'],
       'Department' : ['IT','IT','HR','Accounts']}

df1=pd.DataFrame(exampledict, index=['First','Second','Third','Fourth'])

print(df1)
print("\n")
print(df1['EmpName'])
print("\n")
print(df1['EmpName']['Fourth'])

df1['EmpName']['Fourth']="Ayaan"

filt1=df1['EmpName']=='Ayaan'
print(df1[filt1]['EmpName'])
print("\n")

#df1[filt1]['EmpName']='Ayushi' #this wont work
df1.loc[filt1,'EmpName']='Ayushi'
print(df1)

df1= df1.append({"EmpId":"E05","EmpName":"Amtul"},ignore_index=True)
df1= df1.append({"EmpId":"E06","EmpName":"Kaivalya"},ignore_index=True)

print(df1)

filt1=df1["Department"].isnull()
df1.loc[filt1,'Department']="Not Assigned"
print(df1)

df1['Department'].replace({"Not Assigned": "Unassigned"},inplace=True)
print(df1)

df1['DeptNo']=df1['Department'].map({"IT":1,"HR":2,"Accounts":3})
df1['DeptNo'].fillna("N/A",inplace=True)
print(df1)

# def fun1(x):
#        x='Unassigned'
#        return x
#
# print("\n")
# df1['Department']=df1.loc[filt1,'Department'].replace(fun1)
# print(df1)

exampledict2= {'EmpId': ['E07', 'E08', ],
 'EmpName': ['Lovaraj', 'Soumya']}

df2=pd.DataFrame(exampledict2)

print(df2)

df1=df1.append(df2,ignore_index=True)
print(df1)

print("\n")
#drop row

filt2=df1["Department"].isnull()
print(df1[filt2])

filt3=df1["EmpName"]=='Soumya'
print(df1[filt3].index)
#df1=df1.drop(index=7)

print("drop :- \n")
df1=df1.drop(index=df1[filt2].index)
print(df1)