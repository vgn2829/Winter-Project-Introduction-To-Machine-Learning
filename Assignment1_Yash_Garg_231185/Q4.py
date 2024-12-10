import pandas as pd
import numpy as np
data = {
    "A": np.random.choice([1, 2, 3, np.nan], size=10),
    "B": np.random.choice([10, 20, 30, np.nan], size=10),
    "C": np.random.choice([100, 200, 300, np.nan], size=10),
}
df = pd.DataFrame(data)
df_filled = df.copy()
df_filled = df_filled.fillna(df_filled.mean())

df_sorted = df_filled.sort_values(by=["A", "B"], ascending=[True, False])

# Display the DataFrames
print("Original DataFrame:")
print(df)
print("\nDataFrame after replacing NaN values:")
print(df_filled)
print("\nDataFrame sorted by columns 'A' and 'B':")
print(df_sorted)


