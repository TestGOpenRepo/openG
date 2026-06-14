import re


PATTERNS = [

    r'UTR[:\-]?\s*([A-Z0-9]+)',

    r'[A-Z]{4}\d{8,}',

    r'\d{10,}'
]


def extract_reference(text):

    if text is None:

        return ""

    text = str(text)

    for pattern in PATTERNS:

        match = re.search(
            pattern,
            text
        )

        if match:

            return match.group(0)

    return ""
