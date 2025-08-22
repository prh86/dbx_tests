import pandas as pd

def resample(df: pd.DataFrame, col: str, freq: str) -> pd.DataFrame:
    """Resample dataframe based on the set frequency

    :param df: input dataframe
    :type df: pd.DataFrame
    :return: resampled dataframe
    :rtype: pd.DataFrame
    """
    df_resampled = df.copy()
    df_resampled = df_resampled.set_index(col)
    df_resampled = df_resampled.reindex(
        pd.date_range(start=df_resampled.index.min(), end=df_resampled.index.max(), freq=freq)
    )
    df_resampled = df_resampled.reset_index().rename(columns={"index": col})
    return df_resampled
