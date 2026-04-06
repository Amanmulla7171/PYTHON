import pandas as pd

data={
    "Name":['Ram','aman','sham'],
    "Age":[10,20,30],
    "city":['pune','thane','delhi']
}

df=pd.DataFrame(data)
df.to_csv("data")
df.to_excel("datasample.xlsx")
df.to_excel('sample.xlsx')
print(df.info())
print(df.head(2))
print(df.describe)