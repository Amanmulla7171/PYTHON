import pandas as pd

data={
   "name":['aman','ram','sham','mohan','karan'],
   "age":[20,23,12,13,40],
   "Salary":[10000,3929,2919,2832,3621],
   "Perfomrmance_score":[90,82,37,89,39]
}

df=pd.DataFrame(data)

df.loc[0,'Salary']=100000
print(df)