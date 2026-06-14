import pandas as pd
from pathlib import Path

from matching.match_manager import (
    MatchManager
)

from matching.reference_match import (
    run_reference_match
)

from matching.exact_match import (
    run_exact_match
)

from matching.date_tolerance_match import (
    run_date_tolerance_match
)

# -----------------------------------
# Load preprocessed files
# -----------------------------------

bank_df = pd.read_excel(
    "data/output/01_Bank_Preprocessed.xlsx"
)

gl_df = pd.read_excel(
    "data/output/02_GL_Preprocessed.xlsx"
)

output_dir = Path(
    "data/output"
)

manager = MatchManager()

all_matches = []

# -----------------------------------
# Reference Match
# -----------------------------------

bank_unmatched = (
    manager.get_unmatched_bank(
        bank_df
    )
)

gl_unmatched = (
    manager.get_unmatched_gl(
        gl_df
    )
)

reference_match = (
    run_reference_match(
        bank_unmatched,
        gl_unmatched
    )
)

reference_match.to_excel(
    output_dir /
    "02_Reference_Match.xlsx",
    index=False
)

manager.mark_matched(
    reference_match[
        "BANK_ROW_ID"
    ].unique(),

    reference_match[
        "GL_ROW_ID"
    ].unique()
)

all_matches.append(
    reference_match
)

# -----------------------------------
# Exact Match
# -----------------------------------

bank_unmatched = (
    manager.get_unmatched_bank(
        bank_df
    )
)

gl_unmatched = (
    manager.get_unmatched_gl(
        gl_df
    )
)

exact_match = (
    run_exact_match(
        bank_unmatched,
        gl_unmatched
    )
)

exact_match.to_excel(
    output_dir /
    "01_Exact_Match.xlsx",
    index=False
)

manager.mark_matched(
    exact_match[
        "BANK_ROW_ID"
    ].unique(),

    exact_match[
        "GL_ROW_ID"
    ].unique()
)

all_matches.append(
    exact_match
)

# -----------------------------------
# Date Match
# -----------------------------------

bank_unmatched = (
    manager.get_unmatched_bank(
        bank_df
    )
)

gl_unmatched = (
    manager.get_unmatched_gl(
        gl_df
    )
)

date_match = (
    run_date_tolerance_match(
        bank_unmatched,
        gl_unmatched
    )
)

date_match.to_excel(
    output_dir /
    "03_Date_Tolerance_Match.xlsx",
    index=False
)

manager.mark_matched(
    date_match[
        "BANK_ROW_ID"
    ].unique(),

    date_match[
        "GL_ROW_ID"
    ].unique()
)

all_matches.append(
    date_match
)

# -----------------------------------
# Remaining unmatched
# -----------------------------------

unmatched_bank = (
    manager.get_unmatched_bank(
        bank_df
    )
)

unmatched_gl = (
    manager.get_unmatched_gl(
        gl_df
    )
)

unmatched_bank.to_excel(
    output_dir /
    "07_Unmatched_Bank.xlsx",
    index=False
)

unmatched_gl.to_excel(
    output_dir /
    "08_Unmatched_GL.xlsx",
    index=False
)

# -----------------------------------
# All Matches
# -----------------------------------

all_match_df = pd.concat(
    all_matches,
    ignore_index=True
)

all_match_df.to_excel(
    output_dir /
    "09_All_Matches.xlsx",
    index=False
)

# -----------------------------------
# Summary
# -----------------------------------

summary = pd.DataFrame({

    "Metric": [

        "Bank Records",
        "GL Records",

        "Reference Matches",
        "Exact Matches",
        "Date Matches",

        "Unmatched Bank",
        "Unmatched GL"
    ],

    "Value": [

        len(bank_df),
        len(gl_df),

        len(reference_match),
        len(exact_match),
        len(date_match),

        len(unmatched_bank),
        len(unmatched_gl)
    ]
})

summary.to_excel(
    output_dir /
    "10_Reconciliation_Summary.xlsx",
    index=False
)

print("Part 2 completed successfully")