from dataclasses import dataclass

from models.enums import MatchType


@dataclass

class MatchResult:

    bank_row_id: int

    gl_row_id: int

    bank_amount: float

    gl_amount: float

    match_type: MatchType

    confidence_score: float

    comments: str
