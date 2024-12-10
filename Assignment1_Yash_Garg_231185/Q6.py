import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

grouped_sum = df.groupby('Category')['Value'].sum()

print(grouped_sum)
