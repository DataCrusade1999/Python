import pandas as pd
import numpy as np
import re
print(pd.set_option('display.max_rows',None))
print(pd.set_option('display.max_columns',None))
print(pd.set_option('display.width' ,None))
print(pd.set_option('display.max_colwidth' ,900))

# ZOMATO RESTAURANTS


Zomato=pd.read_csv('Restaurant names and Metadata.csv')



print(Zomato)
print(Zomato.head(5)) #<--- Top 5 Data Entries
print(Zomato.tail(5)) #<--- Bottom 5 Data Entries
print(pd.read_csv('data.txt',delimiter=','))
print(Zomato.columns) #<---- For Header's
print(Zomato.Name)
print(Zomato['Name'][0:5])
print(Zomato[['Name','Links']])
print(Zomato.iloc[1:4])
print(Zomato.iloc[1]) #iloc Stands For Integer Location
print(Zomato.iloc[1,1]) #Array Style Indexing


for index,row in Zomato.iterrows():
    print(index,row)


print(Zomato.describe()) #<--- Describing Important Metrics About The Data
print(Zomato.loc[Zomato["Cuisines"]=="North Indian"]) #<--- Use This When Searching For A Particular Thing

print(Zomato.sort_values('Name'))
print(Zomato.sort_values("Name",ascending=False)) #<-- Starts From The Bottom

print(Zomato[['Name','Cost']].sort_values(['Name','Cost'],ascending=[1,0]))
print(Zomato.sort_values(['Name','Cost'],ascending=[1,1]))

print(Zomato.drop(columns='Cost')) #<--- Dropping A Particular Column

#print(Zomato.iloc[:,2].sort_values(ascending=True))


#print(Zomato.iloc[:,2].sum(axis=0))


#print(Zomato.loc[(Zomato['Price']==500) & (Zomato['Cuisine'=='Chinese'])])

print(Zomato.sort_values(['Name','Cost'],ascending=[1,1]))
New_Zomato=Zomato.sort_values(['Name','Cost'],ascending=[1,1])
print(New_Zomato.reset_index())
print(New_Zomato.reset_index(drop=True, inplace=True))
print(Zomato)
print(Zomato.loc[Zomato['Name'].str.contains('Chinese')])
print(Zomato.loc[~Zomato['Name'].str.contains('Chinese')])
df = pd.DataFrame(np.random.randn(6, 4))
print(df.describe())
print(df.T)
print(df.iat[1,1])
print(df.mean())
print(Zomato)
print(Zomato.loc[Zomato['Name'].str.contains('chinese|indian',flags=re.I,regex=True)])
Zomato_1=Zomato.loc[Zomato['Name']=='Chinese','Name']='Indian'
print(Zomato_1)
print(Zomato.groupby(['Name']).count())
