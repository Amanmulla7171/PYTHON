import pandas as pd
import numpy as np

# From a dictionary
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "age": [25, 30, 27],
    "salary": [60000, 75000, 68000]
})

# From a list of lists
df2 = pd.DataFrame([["X", 1], ["Y", 2]], columns=["label", "value"])

# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# Range of numbers
df3 = pd.DataFrame({"x": np.arange(10), "y": np.random.randn(10)})

df.head()          # first 5 rows
df.tail(3)         # last 3 rows
df.shape           # (rows, cols)
df.dtypes          # column data types
df.columns         # column names
df.index           # row index
df.info()          # summary + nulls
df.describe()      # stats (mean, std, min, max…)
df.value_counts()  # frequency of each unique value

# Add a new column
df["bonus"] = df["salary"] * 0.1

# Computed column with apply
df["senior"] = df["age"].apply(lambda x: x >= 28)

# Rename columns
df.rename(columns={"name": "employee"}, inplace=True)

# Drop a column
df.drop(columns=["bonus"], inplace=True)

# Change dtype
df["age"] = df["age"].astype("float")