import pandas as pd
import numpy as np

## Random Baseline
# load test dataset
df = pd.read_csv("test.csv")

# define tone labels
tones = ["optimistic", "informative", "suspenseful", "inspirational", "poetic", "pessimistic", "humorous"]

# assign random predictions
np.random.seed(42)
df["ground_truth"] = np.random.choice(tones, size=len(df))

# save random baseline predictions to a new file
df.to_csv("predictions.csv", index=False)


## Majority Baseline
# load train dataset to determine the most common tone
train_df = pd.read_csv("train.csv")
most_common_tone = train_df["ground_truth"].mode()[0]  # Find the most common label in train.csv

# load test dataset again
df = pd.read_csv("test.csv")

# assign this tone to all predictions
df["ground_truth"] = most_common_tone

# Save majority baseline predictions to a new file
df.to_csv("predictions.csv", index=False)


