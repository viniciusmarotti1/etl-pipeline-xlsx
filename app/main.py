from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.load import load

if __name__ == "__main__":  
    df_list = extract("data/input")
    print(type(df_list))

    df = transform(df_list)
    print(type(df))
    
    load(df, "data/output", "output")