import pandas as pd
from app.pipeline.transform import transform

df_1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df_2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

def test_transform_df_list():
    arrange = pd.concat([df_1, df_2], ignore_index=True)
    act = transform([df_1, df_2])

    assert arrange.equals(act)