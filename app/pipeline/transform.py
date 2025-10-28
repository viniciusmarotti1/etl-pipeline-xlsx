import pandas as pd
from typing import List


def transform(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(df_list, ignore_index=True)