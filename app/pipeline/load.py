import pandas as pd
import os

def load(df: pd.DataFrame, output_path: str, file_name: str) -> str:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    df.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return f"{output_path}/{file_name}.xlsx"
