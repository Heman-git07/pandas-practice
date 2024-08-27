#by using index argument,you can add your convenient labels(to select paricular values)
import pandas as pd
data=["heman","muthu","akash","srinath"]
var=pd.Series(data,index=["a","b","c","d"])
print(var["a"])#print the first value of list

