import pandas as pd

def run_reference_match(bank_df, gl_df):

    results = []

    reference_pairs = [
        ("BANK_REF_CLEAN", "REFERENCE_CLEAN"),
        ("BANK_REF_CLEAN", "ASSIGNMENT_CLEAN"),
        ("BANK_REF_CLEAN", "REFERENCE_KEY_CLEAN"),

        ("CUSTOMER_REF_CLEAN", "REFERENCE_CLEAN"),
        ("CUSTOMER_REF_CLEAN", "ASSIGNMENT_CLEAN"),
        ("CUSTOMER_REF_CLEAN", "REFERENCE_KEY_CLEAN"),

        ("EXTRACTED_REFERENCE", "REFERENCE_CLEAN")
    ]

    for bank_col, gl_col in reference_pairs:

        if gl_col not in gl_df.columns:
            continue

        temp = bank_df.merge(
            gl_df,
            left_on=["BANK_AMOUNT", bank_col],
            right_on=["GL_AMOUNT", gl_col],
            how="inner"
        )

        if len(temp) > 0:

            temp["MATCH_TYPE"] = "REFERENCE"
            temp["CONFIDENCE"] = 100

            results.append(temp)

    if len(results) == 0:
        return pd.DataFrame()

    return pd.concat(results, ignore_index=True)