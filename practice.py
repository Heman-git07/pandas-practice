import pandas as pd
a=[1,2,3,4]
var=pd.Series(a,index=["a","b","c","d"])
print(var["c"])