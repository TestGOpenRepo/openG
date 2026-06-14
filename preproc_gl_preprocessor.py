import pandas as pd
import numpy as np

from preprocessing.text_cleaner import (
    clean_text
)


class GLPreprocessor:


    def process(self, gl_df):

        gl_df = gl_df.copy()

        gl_df["GL_ROW_ID"] = range(
            1,
            len(gl_df) + 1
        )

        gl_df[
            "Posting Date"
        ] = pd.to_datetime(
            gl_df[
                "Posting Date"
            ]
        )

        gl_df[
            "GL_AMOUNT"
        ] = np.where(
            gl_df[
                "Posting Key"
            ].astype(str) == "50",

            gl_df[
                "Amount in local currency"
            ].abs(),

            -gl_df[
                "Amount in local currency"
            ].abs()
        )

        gl_df[
            "REFERENCE_CLEAN"
        ] = (
            gl_df[
                "Reference"
            ]
            .fillna("")
            .apply(clean_text)
        )

        gl_df[
            "ASSIGNMENT_CLEAN"
        ] = (
            gl_df[
                "Assignment"
            ]
            .fillna("")
            .apply(clean_text)
        )

        gl_df[
            "REFERENCE_KEY_CLEAN"
        ] = (
            gl_df[
                "Reference Key"
            ]
            .fillna("")
            .apply(clean_text)
        )

        gl_df["MATCHED"] = False

        return gl_df
