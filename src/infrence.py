import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

example = [[5.1, 3.5, 1.4, 0.2]]

pred = model.predict(example)

print("Predicted Species:", pred[0])