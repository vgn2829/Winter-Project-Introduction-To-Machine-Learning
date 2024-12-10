import pandas as pd
import numpy as np

data1 = {
    'id': np.arange(1, 11), 
    'Feature1': np.random.randint(10, 100, 10),
    'Feature2': np.random.rand(10)
}
df1 = pd.DataFrame(data1)

#
data2 = {
    'id': np.arange(6, 16),  
    'Feature3': np.random.randint(100, 200, 10),
    'Feature4': np.random.rand(10)
}
df2 = pd.DataFrame(data2)


merged_df = pd.merge(df1, df2, on='id', how='inner')  
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
print("\nMerged DataFrame:\n", merged_df)
