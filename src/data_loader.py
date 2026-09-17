import pandas as pd
from pathlib import Path
DATA_PATH=Path(__file__).resolve().parents[1]/"data"/"courses.csv"
def load_courses(path=DATA_PATH):
    df=pd.read_csv(path)
    required=["course","domain","level","keywords"]
    missing=[c for c in required if c not in df.columns]
    if missing: raise ValueError(f"Missing columns: {missing}")
    if df.empty: raise ValueError("Course dataset is empty.")
    return df
