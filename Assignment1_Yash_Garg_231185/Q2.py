import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
iris_df = pd.DataFrame(
    data=iris.data, 
    columns=iris.feature_names
)
arr=iris_df[iris.feature_names[2]]>3.0
filtered_df = iris_df[arr]

print(filtered_df)