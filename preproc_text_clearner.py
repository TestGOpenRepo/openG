import re
import pandas as pd


def clean_text(value):

    if pd.isna(value):
        return ""

    value = str(value)

    value = value.upper()

    value = value.strip()

    value = re.sub(
        r"[^A-Z0-9]",
        "",
        value
    )

    return value
