import pandas as pd

def create_dataframe(rules):
    return pd.DataFrame(rules)

def export_to_csv(df, output_path):
    df.to_csv(output_path, index=False)