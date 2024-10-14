import pandas
df = pandas.read_csv('players_23.csv',sep=',')
# df = pandas.read_csv('players_23.csv', header = 2)
# df = pandas.read_csv('players_23.csv',encoding = 'ISO-8859-1')
#these are common issues that occur, first one is if the values is serperated by other values than commas.
#2 is to set a header to that specific row (2) in this case
#3 is for an error message that can appear.
print(df)
print(df.shape)
print(len(df.columns))#9,10,11 are for rows and columns
print(len(df))
print(df['long_name'])#returns all values of this specific column
print(df.iloc[2]) #gets rows and/or columns in integer locations.
print(df.iloc[2:5][['short_name','club_name']])#range of rows
print(df.iloc[:5])#gets first 5 rows, add - to get last 5
print(df.loc[2])#gets rows/colums with labels
#how to make a data frame
data = {'Name':['Tom','Jack','Nick','Juli'],'marks':[99,58,35,40]}
createdf = pandas.DataFrame(data)#how to make a data frame
print(createdf)
createdf.to_csv('file_name.csv')
