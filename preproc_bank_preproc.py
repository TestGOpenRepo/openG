import pandas as pd

from preprocessing.text_cleaner import (
    clean_text
)

from preprocessing.reference_extractor import (
    extract_reference
)


class BankPreprocessor:


    def process(self, bank_df):

        bank_df = bank_df.copy()

        bank_df["BANK_ROW_ID"] = range(
            1,
            len(bank_df) + 1
        )

        bank_df[
            "Transaction Date"
        ] = pd.to_datetime(
            bank_df[
                "Transaction Date"
            ]
        )

        bank_df[
            "BANK_AMOUNT"
        ] = (
            bank_df[
                "Credit Amount"
            ].fillna(0)
            -
            bank_df[
                "Debit Amount"
            ].fillna(0)
        )

        bank_df[
            "CUSTOMER_REF_CLEAN"
        ] = (
            bank_df[
                "Customer Reference"
            ]
            .fillna("")
            .apply(clean_text)
        )

        bank_df[
            "BANK_REF_CLEAN"
        ] = (
            bank_df[
                "Bank Reference"
            ]
            .fillna("")
            .apply(clean_text)
        )

        bank_df[
            "EXTRACTED_REFERENCE"
        ] = (
            bank_df[
                "Description"
            ]
            .fillna("")
            .apply(extract_reference)
        )

        bank_df["MATCHED"] = False

        return bank_df
