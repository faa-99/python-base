from typing import List, Union

import pandas as pd


def drop_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows that contain NaN values
    df.dropna(axis=0)
    """
    return df.dropna().reset_index(drop=True)


def drop_all_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows that have all NaN values
    """
    return df.dropna(how="all")


def drop_subset_nan(df: pd.DataFrame, cols: List) -> pd.DataFrame:
    """
    Drop rows that have NaN values in specific columns
    """
    return df.dropna(subset=cols)


def drop_rows(df: pd.DataFrame, rows: Union[int, str, List]) -> pd.DataFrame:
    """

    :param df: original dataframe
    :param rows: row name, index, or list of row names
    :return: dataframe with dropped rows
    """
    return df.drop(rows, axis=0)


def drop_cols(df: pd.DataFrame, cols: Union[int, str, List]) -> pd.DataFrame:
    """

    :param df: original dataframe
    :param cols: col name, index, or list of col names
    :return: dataframe with dropped rows
    """
    return df.drop(cols, axis=1)


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """

    :param df: dataframe with duplicates
    :return: re-indexed df without duplicates

    df.drop_duplicates(keep='last')
    df.drop_duplicates(subset=['c'])

    """
    return df.drop_duplicates().reset_index(drop=True)


def replace_nan(df: pd.DataFrame, value) -> pd.DataFrame:
    """

    :param df: dataframe with NaN
    :param value: replace value of NaN
    :return: dataframe with replaced NaN
    """
    return df.fillna(value)
