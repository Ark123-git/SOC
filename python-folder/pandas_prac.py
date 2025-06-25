import pandas as pd
file=pd.read_csv("pokemon_data.csv")
# print(file)
# Read file-     xyz=pd.read_filetype(“filename”)
# print(xyz)
# Top-print(xyz.head(3))
# Bottom-print(xyz.tail(2))
# print(file.head(4))
# print(file.tail(4))
# file_txt=pd.read_csv("pokmon_data.txt",delimiter='\t')     (tab)

# Read headers
# print(file.columns)
# print(file['Type 1'])
# print(file['Type 1'][0:5])
# print(file[['Type 1','Name']][0:5])

#FOr printing rows use iloc(interger location)
# print(file.iloc[0])
# print(file.iloc[0:3])
# print element
# print(file.iloc[0,2])

# Another way use a for loop
# i->index j->row
# for i,j in file.iterrows(): 
#     print(i,j)
# for i,j in file.iterrows(): 
#      print(i,j['Name'])

# print(file.loc[file['Type 1']=='Fire'])



# Stats
# print(file.describe())

# sorting of file
# print(file.sort_values('Name'))
# file.sort_values('Name')
# print(file)(does not change orignial file)
# print(file.sort_values('Name',ascending=False))
# print(file.sort_values(['Name','HP'],ascending=[0,1]))



# Make changes
file['Total']=file['Attack']+file['HP']
# # print(file.iloc[0])
# file=file.drop(columns=['Total'])
# print(file.iloc[0])
# axis=1 horizontal iloc->[rows,columns]      END PARAMETER IS EXCLUSIVE
# file['Total']=file.iloc[:,4:6].sum(axis=1)
# print(file.iloc[2:4])

# re order columns
# col_values=list(file.columns.values)
# file=file[col_values[0:4]+[col_values[-1]]+col_values[4:12]]
# print(file.iloc[0])
# file.to_csv('Modified.csv',index=False)

# filtering Data
# print(file.loc[(file['Type 1']=='Grass') & (file['Type 2']=='Poison')])
# print(file.loc[file['Name'].str.contains('Mega')])
# print(file.loc[~(file['Name'].str.contains('Mega'))])
import re
# file.loc[file['Name'].str.contains(('fire|grass'),regex=True,flags=re.I)]
# ^->start of line 
# [a-z]* next letters can be from a-z *-> zero or more letteers can be there
#re.I  case insensitive (regex -regular expression )
# print(file.loc[file['Name'].str.contains(('^pi[a-z]*'),regex=True,flags=re.I)])
file.loc[file['Type 1']=='Fire','Type 1']='Flame'
# print(file[['Type 1','Name']])
# file.loc[file['Total']>200,['Generation','Legendary']]='Test val'
# file.loc[file['Total']>200,['Generation','Legendary']]=['Test val','yes']

print(file.groupby(['Type 1']).mean(numeric_only=True).sort_values('Attack',ascending=False))




          
