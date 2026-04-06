import pandas as pd

df_customer=pd.DataFrame({
    'Customer_Id':[1,2,3],
    'Name':["ram","rahim","anthoni"]
})

df_ordered=pd.DataFrame({
    'Customer_Id':[1,2,4],
    'OrderAmount':[292,281,389]
})

df_merge=pd.merge(df_customer,df_ordered, on="Customer_Id",how="inner")
print(df_merge)

df_merge=pd.merge(df_customer,df_ordered, on="Customer_Id",how="outer")
print(df_merge)

df_merge=pd.merge(df_customer,df_ordered, on="Customer_Id",how="left")
print(df_merge)

df_merge=pd.merge(df_customer,df_ordered, on="Customer_Id",how="cross")
print(df_merge)
