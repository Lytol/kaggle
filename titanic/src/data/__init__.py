import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]

train_path = project_dir / "data/raw/train.csv"
test_path = project_dir / "data/raw/test.csv"

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
