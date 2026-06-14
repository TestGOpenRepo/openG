def run_exact_match(bank_df, gl_df):

    result = bank_df.merge(
        gl_df,
        left_on=[
            "BANK_AMOUNT",
            "Transaction Date"
        ],
        right_on=[
            "GL_AMOUNT",
            "Posting Date"
        ],
        how="inner"
    )

    result["MATCH_TYPE"] = "EXACT"
    result["CONFIDENCE"] = 95

    return result