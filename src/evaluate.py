import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import json

df = pd.read_csv("data/processed.csv")
model = joblib.load("models/model.pkl")

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

accuracy = model.score(X_test, y_test)

metrics = {"accuracy": accuracy}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Evaluation done. Accuracy:", accuracy)