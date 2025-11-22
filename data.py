from sklearn.datasets import load_iris
import pandas as pd

df = pd.DataFrame(load_iris().data, columns=[
    "sepal_length", "sepal_width", "petal_length", "petal_width"
])
df["species"] = load_iris().target
df.to_csv("data/raw/iris.csv", index=False)
print("Iris dataset saved to data/raw/iris.csv")