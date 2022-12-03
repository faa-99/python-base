import pandas as pd


def apply_fnc_on_axis(df: pd.DataFrame, fnc, axis: int = 0) -> pd.DataFrame:
    """

    :param df: dataframe
    :param fnc: function to apply on row/ col
    :param axis: 0 for cols and 1 for rows
    :return: dataframe with the applied function

    Example of functions:
        1. np.sqrt
        2. np.sum
        3. lambda x: np.square(x) if x.name == 'd' else x
    """
    return df.apply(fnc, axis=axis)


def apply_fnc_elementwise(df: pd.DataFrame, fnc, na_action: str = None) -> pd.DataFrame:
    """

    :param df: dataframe
    :param fnc: function to apply on each element in df
    :param na_action: how to deal with NA values: 'ignore' or None
    :return: dataframe with applied fnc

    Examples of functions:
        1. lambda x: x**2
    """

    return df.applymap(fnc, na_action)


def apply_fnc_elementwise_ser(ser: pd.Series, mapping, na_action: str = None) -> pd.Series:
    """
    Used for substituting each value in a Series with another value
    :param ser: Series
    :param mapping: mapping to apply
    :param na_action: how to deal with NA values: 'ignore' or None
    :return: Series with applied mapping

    Examples of mappings:
        1. function:
            'I am a {}'.forma
        2. Dictionary:
            {'cat': 'kitten', 'dog': 'puppy'}
        3. Series

    """

    return ser.map(mapping, na_action)
