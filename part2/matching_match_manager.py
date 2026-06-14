# matching/match_manager.py

class MatchManager:

    def __init__(self):
        self.matched_bank_ids = set()
        self.matched_gl_ids = set()

    def mark_matched(self, bank_ids, gl_ids):

        self.matched_bank_ids.update(bank_ids)
        self.matched_gl_ids.update(gl_ids)

    def get_unmatched_bank(self, bank_df):

        return bank_df[
            ~bank_df["BANK_ROW_ID"].isin(
                self.matched_bank_ids
            )
        ]

    def get_unmatched_gl(self, gl_df):

        return gl_df[
            ~gl_df["GL_ROW_ID"].isin(
                self.matched_gl_ids
            )
        ]