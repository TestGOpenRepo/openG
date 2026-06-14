from dataclasses import dataclass
from datetime import datetime

from models.enums import (
    SourceType,
    MatchStatus
)


@dataclass

class Transaction:

    row_id: int

    source: SourceType

    transaction_date: datetime

    amount: float

    reference: str

    description: str

    document_number: str = ""

    assignment: str = ""

    account: str = ""

    posting_key: str = ""

    match_status: MatchStatus = (
        MatchStatus.UNMATCHED
    )
