import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    valid_name = r"^[A-Za-z_]+$"

    # Validate new column
    if not re.match(valid_name, new_column):
        return pd.DataFrame([])

    # Validate dataframe columns
    for col in df.columns:
        if not re.match(valid_name, col):
            return pd.DataFrame([])

    
    role = role.strip().replace(" ", "")

    
    if not re.match(r"^[A-Za-z_+\-*]+$", role):
        return pd.DataFrame([])

    
    match = re.search(r"[+\-*]", role)

    if not match:
        return pd.DataFrame([])

    operator = match.group()
    parts = role.split(operator)

    if len(parts) != 2:
        return pd.DataFrame([])

    col1, col2 = parts

    
    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])

    try:
        if operator == "+":
            result = df[col1] + df[col2]

        elif operator == "-":
            result = df[col1] - df[col2]

        elif operator == "*":
            result = df[col1] * df[col2]

        else:
            return pd.DataFrame([])

    except Exception:
        return pd.DataFrame([])

    new_df = df.copy()
    new_df[new_column] = result

    return new_df
