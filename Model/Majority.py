import pandas as pd
import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score, classification_report

## Random Baseline
# load dataset
df = pd.read_csv("compiled_annotations.csv")

# all possible tone labels
tones = ["Suspenseful", "Inspirational", "Poetic", "Pessimistic", "Informative"]

# assign a random label
np.random.seed(42)
df["Random_Tone"] = np.random.choice(tones, size=len(df))

# save file
df.to_csv("random_baseline_predictions.csv", index=False)

# compare random generated labels to actual labels:
df = pd.read_csv("random_baseline_predictions.csv")

annotator_columns = [col for col in df.columns if "Annotator" in col]
df["Actual_Tones"] = df[annotator_columns].apply(lambda row: set(row.dropna()), axis=1)

# check if the random label matches any of the actual labels
df["Correct"] = df.apply(lambda row: row["Random_Tone"] in row["Actual_Tones"], axis=1)

# calculate accuracy
accuracy = df["Correct"].mean()
print(f"Random Baseline Accuracy: {accuracy:.4f}")

# Convert data for classification report
y_true = []
y_pred = []

for _, row in df.iterrows():
    if row["Actual_Tones"]:  # Avoid empty rows
        y_true.append(next(iter(row["Actual_Tones"])))
        y_pred.append(row["Random_Tone"])

# Generate classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=["Optimistic", "Humorous", "Suspenseful", "Inspirational", "Poetic", "Pessimistic", "Informative"]))

