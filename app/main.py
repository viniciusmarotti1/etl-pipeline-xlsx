from pipeline.extract import extract

df_list = extract("data/input")
print(f"Number of dataframes extracted: {len(df_list)}")