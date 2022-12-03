import numpy as np
import pandas as pd


"""
Use zip() when possible
When the index is needed, use itertuples().
"""

ROWS = 10000

# Create a dummy dataframe with 3 columns representing 3 different features
df = pd.DataFrame(
    {
        "feature_1": np.random.normal(size=ROWS),
        "feature_2": np.random.normal(size=ROWS),
        "feature_3": np.random.normal(size=ROWS),
    }
)


def using_itertuples():
    row_sum = 0
    indices = []
    for row in df.itertuples():
        indices.append(row[0])
        row_sum += row[1] + row[2] + row[3]
    return row_sum


def using_zip():
    row_sum = 0
    for row in zip(df["feature_1"], df["feature_2"], df["feature_3"]):
        row_sum += row[0] + row[1] + row[2]
    return row_sum


def using_range():
    row_sum = 0
    for i in range(df.shape[0]):
        row_sum += (
            df["feature_1"].values[i]
            + df["feature_2"].values[i]
            + df["feature_3"].values[i]
        )
    return row_sum
