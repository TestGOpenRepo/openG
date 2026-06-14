import pandas as pd

from preprocessing.bank_preprocessor import (
    BankPreprocessor
)

from preprocessing.gl_preprocessor import (
    GLPreprocessor
)


bank_df = pd.read_excel(
    "data/input/bank_statement.xlsx"
)

gl_df = pd.read_excel(
    "data/input/gl_data.xlsx"
)


bank_processor = (
    BankPreprocessor()
)

gl_processor = (
    GLPreprocessor()
)


bank_df = (
    bank_processor.process(
        bank_df
    )
)

gl_df = (
    gl_processor.process(
        gl_df
    )
)

print(
    "Preprocessing completed"
)
