#label
#label(used to specify particular value using index number)
import pandas as pd
data=["car","bike","boat","train"]
var=pd.Series(data)
print(var[2]) #selecting 3rd value using index number 2
#output:boat
