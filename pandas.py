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


