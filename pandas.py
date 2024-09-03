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
