import os
import glob
import pandas as pd
from typing import List
"""
    Função para ler os arquivos xlsx (data/input) para retornar uma lista de DF
    arg: input path
    ret: list DF
"""
path = "data/input"
def extract(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    df_list = []

    for file in all_files:
        df_list.append(pd.read_excel(file))

    return df_list

if __name__ == "__main__":
    result = extract(path)
    print(result)