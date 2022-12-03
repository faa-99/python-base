import pandas as pd
import numpy as np

if __name__ == "__main__":
    ROWS = 10000

    # Create a dummy dataframe with 3 columns representing 3 different features
    df = pd.DataFrame(
        {
            "feature_1": np.random.normal(size=ROWS),
            "feature_2": np.random.normal(size=ROWS),
            "feature_3": np.random.normal(size=ROWS)
        }
    )

    print(df.max())
    print(df.min())
    print(df.mean())
    print(df.count())
    print(df.sum())

    print(df.shape)

    print(df.clip(lower=1, upper=10))

    print(df.describe())

    print(df.duplicated().any())
    print(df.isnull().values.any())
    print(df.isnull().values.sum())

    print(df.value_counts())
    print(df.nunique())
    for col in df:
        print(df[col].unique())
        print(df[col].value_counts())
