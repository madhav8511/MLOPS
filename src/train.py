import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import yaml
import json

# Load params
params = yaml.safe_load(open("params.yaml"))
max_depth = params["train"]["max_depth"]

df = pd.read_csv("data/processed.csv")

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=max_depth)
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")

print("Model trained!")