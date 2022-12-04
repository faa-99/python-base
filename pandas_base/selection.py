from typing import List

import pandas as pd


def select_unique_col_vals(df: pd.DataFrame, col_name: str):
    return df[col_name].unique()


def select_cols_with_nans(df: pd.DataFrame):
    return df.loc[:, df.isnull().any()]


def select_cols_without_nans(df: pd.DataFrame):
    return df.loc[:, df.notnull().all()]


def select_random_fraction_rows(
        df: pd.DataFrame, fraction: float = 0.5, reindex: bool = True
) -> pd.DataFrame:
    df_sample = df.sample(frac=fraction)
    if reindex:
        df_sample = df_sample.reset_index(drop=True)
    return df_sample


def select_random_number_rows(
        df: pd.DataFrame, number: int, reindex: bool = True
) -> pd.DataFrame:
    df_sample = df.sample(n=number)
    if reindex:
        df_sample = df_sample.reset_index(drop=True)
    return df_sample


def split_rows_on_condition(df: pd.DataFrame, mask: pd.Series):
    """

    :param df: dataframe to split
    :param mask: series with boolean indices coming from a condition applied
    :return:

    Example of masks:
        1. df["feature_1"] > value
    """

    return df[mask], df[~mask]


def select_rows_with_value(df: pd.DataFrame, col: str, value):
    return df.loc[df[col] == value]


def select_rows_with_value_list(df: pd.DataFrame, col: str, values: List):
    return df.loc[df[col].isin(values)]


def select_all_cols_except(df: pd.DataFrame, except_cols: List[str]):
    return df[df.columns.difference(except_cols)]


def set_value_on_condition(
        df: pd.DataFrame, condition_col, condition_val, set_col, set_val
):
    """
    Set a value in a column when another value in another column meets a certain condition
    Example:
        Set the value of column A to 0 when value in column B is equal to 100.
    :param set_val:
    :param set_col:
    :param condition_val:
    :param condition_col:
    :param df:
    :return:

    Can be scaled to multiple conditions on multiple columns
        df.loc[
        (df[col_cond1] == value_cond1) & (df[col_cond2] == value_cond2), col_val
            ] = value
    return df

    """
    df.loc[df[condition_col] == condition_val, set_col] = set_val
    return df


def df_intersection(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Return the common rows between the two dfs without duplicates
    :param df1: first df
    :param df2: second df
    :return:
    """
    return pd.merge(df1, df2, how="inner").drop_duplicates()


def select_values_by_range(df, row_ini, row_end, col_ini, col_end):
    """Select a range of values in the dataframe.

    Args:
        df (pd.DataFrame): Dataframe.
        row_ini (int): Initial row.
        row_end (int): Final row.
        col_ini (int): Initial column.
        col_end (int): Final column.

    Returns:
        pd.DataFrame: Dataframe with the specific range of rows and columns.

    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> select_values_by_range(df, 0, 1, "letters", "numbers")
          letters  numbers
        0       a        1
        1       a        2
    """
    return df.loc[row_ini:row_end, col_ini:col_end]


def select_values_by_index(df, vector_row_pos, vector_col_pos):
    """Select values in the dataframe given specific indexes of rows and columns.

    Args:
        df (pd.DataFrame): Dataframe.
        vector_row_pos (array): Array of row positions.
        vector_col_pos (array): Array of column positions.

    Returns:
        pd.DataFrame: Dataframe with the specific values in the row and column indexes.

    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> select_values_by_index(df, vector_row_pos=[0,2], vector_col_pos=[0,1])
          letters  numbers
        0       a        1
        2       c        3
    """
    return df.iloc[vector_row_pos, vector_col_pos]


def select_random_columns(df, n):
    return df.sample(n=n, axis='columns')
