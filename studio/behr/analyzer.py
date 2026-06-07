from .normalizer import normalize_text

from .syllables import (
    syllable_pattern
)

from .rukn import (
    generate_rukn_sequence
)

from .matcher import (
    match_bahr
)


def analyze_behr(text):

    normalized = normalize_text(
        text
    )

    pattern = syllable_pattern(
        normalized
    )

    rukn_sequence = generate_rukn_sequence(
        pattern
    )

    bahr_result = match_bahr(
        rukn_sequence
    )

    return {

        "normalized": normalized,

        "pattern": pattern,

        "rukn_sequence": rukn_sequence,

        "bahr": bahr_result["bahr"],

        "score": bahr_result["score"]

    }