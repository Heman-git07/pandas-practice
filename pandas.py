#install pandas
"""pip install pandas"""
#Once Pandas is installed, import it in your applications by adding the import keyword
"""import pandas"""

#pandas series
#1
import pandas as pd
data=["heman","muthu","saro"]
data_1=pd.Series(data)
print(data_1)
#2we can also select particular value by using index
print(data_1[0])
#3cwe can also set our own index using index word

data_2=["apple","orange","pineapple"]
data_3=pd.Series(data_2,index=["a","b","c"])
print(data_3["c"])

#key/value object in pandas series
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#dataframes
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#selecting particuar data from data set using loc atrribute or return a pandas series
import pandas as pd
dic={"name":["heman","muthu","saro"],"age":[21,22,23],"area":["madurai","aviyur","chennai"]}
a=pd.DataFrame(dic)
print(a)
print(a.loc[1])

#selecting particular pandas dataframe
import pandas as pd
dic={"name":["heman","muthu","saro"],"age":[21,22,23],"area":["madurai","aviyur","chennai"]}
a=pd.DataFrame(dic)
print(a)
print(a.loc[[0,2]])

#create a own label using idex argument in pandas dataframe
import pandas as pd
dic={"rollnum":[1,2,3],"age":[21,22,24]}
v=pd.DataFrame(dic,index=["s1","s2"])
print(v.loc["s1"])

#load files into dataframe
import pandas as pd
df=pd.read_csv("csv file.csv")
print(df)

#to print the entire data in dataset 
import pandas as pd 

df=pd.read_csv("csv file.csv")

print(df.to_string())

#to check maximum row that our systems is returned is achieve through pd.options.display.max_rows

import pandas as pd
print(pd.options.display.max_rows)

#we can also increase the number rows to display by using pd.options.display.max_rows

import pandas as pd

pd.options.display.max_rows=78 #78 is our preference value

df=pd.read_csv("csvfile.csv")

print(df)

#read json file and to load as dataframe
import pandas as pd

df=pd.read_json("json file.json")

print(df.to_string)

#we can directly load the json  data in python without json file,because the data inside the json file is like a dictionary in python
import pandas as pd 
data={
"name":{"0":"heman","1":"muthu","2":"saro"},
"age":{"0":"21","1":"24","2":"23"},
"roll":{"0":"20bec090","1":"20bec091","2":"20nec093"}
}
df=pd.DataFrame(data)
print(df)

#head() function is used to display a selected rows from top order,we can set value inside that function to display the value of rows

import pandas as pd
df=pd.read_csv("csv file")
print(pd.head(10)) #10 rows from top order is printed
print(pd.head()) #first 5 rows from data set is printed

#tail() function is used to display selected last rows from dataset

import pandas as pd
df=pd.read_csv("csv file")
print(pd.tail(10)) #print last 10 row

#info() function is used to display a information about dataframe

import pandas as pd
df=pd.read_csv("csv file")
print(pd.info())

#Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#Remove all rows with NULL values:

import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

#Replace NULL values with the number 130:
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

#Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

#Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

#Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

#Calculate the MODE, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

#data of wrong formate
#Convert to date:
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

#Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

#Replacing Values
#Set "Duration" = 45 in row 7:
df.loc[7, 'Duration'] = 45

#Loop through all values in the "Duration" column.If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
#Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
#removing duplicates
#Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

#Remove all duplicates:
df.drop_duplicates(inplace = True)

#Show the relationship between the columns:
df.corr()

#pandas plotting

#Import pyplot from Matplotlib and visualize our DataFrame:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()






