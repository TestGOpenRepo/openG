from enum import Enum


class SourceType(Enum):

    BANK = "BANK"

    GL = "GL"


class MatchType(Enum):

    REFERENCE = "REFERENCE"

    EXACT = "EXACT"

    DATE_TOLERANCE = "DATE_TOLERANCE"

    ONE_TO_MANY = "ONE_TO_MANY"

    MANY_TO_ONE = "MANY_TO_ONE"

    FUZZY = "FUZZY"


class MatchStatus(Enum):

    UNMATCHED = "UNMATCHED"

    MATCHED = "MATCHED"
