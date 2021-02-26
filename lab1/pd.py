import pandas as pd
import numpy as np

s = pd.Series([3,9,10,5])
print(s.sum())
print(s.min())
print(s.max())

#Dataframes
print("\nData frames")
data = [['Dennis', 3], ['John', 4]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)

#Indexed Data frames
print("\nIndexed Dataframes")
data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

#Create DF using a dictionary
df1=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),
'C':pd.Categorical(['Male','Female','Male','Female'])})

print('\nMetadata')
print(df1)
print(df1.shape)
print(df1.head())
print(df1.tail())

print(df1.index)
print(df1.columns)

#Sort by axis 
print('\nSorting')
df.sort_index(axis=1, ascending=False)

#Slice by rows
dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))
print('\nSlicing')
print(df[0:3])
print(df.iloc[0:2])
print(df.iloc[0:0])
print(df['A'])

#Boolean indexing
print(df[df.A>0])

#Delete a row
df.drop ('A', axis =1, inplace=True)

#COncat 
Df_new= pd.concat (df1, df1, axis=1)
print(Df_new.shape)