def run_date_tolerance_match(
        bank_df,
        gl_df,
        tolerance_days=3
):

    merged = bank_df.merge(
        gl_df,
        left_on="BANK_AMOUNT",
        right_on="GL_AMOUNT"
    )

    merged["DAY_DIFF"] = (
        merged["Transaction Date"]
        -
        merged["Posting Date"]
    ).abs().dt.days

    result = merged[
        merged["DAY_DIFF"] <= tolerance_days
    ]

    result["MATCH_TYPE"] = (
        "DATE_TOLERANCE"
    )

    result["CONFIDENCE"] = 85

    return result