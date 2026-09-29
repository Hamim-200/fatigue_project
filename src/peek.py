import os
import pandas as pd

base = r"N:\CSE498R\fatigue_project\data\Data"

for user in ["user1", "user2"]:
    folder = os.path.join(base, user)
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        print("=" * 70)
        print(user, "|", name)
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            n_lines = sum(1 for _ in f)
        print("Total lines:", n_lines)
        df = pd.read_csv(path, sep="\t", nrows=5, encoding="utf-8",
                         encoding_errors="replace", on_bad_lines="skip")
        print("Columns:", list(df.columns))
        print(df.to_string())