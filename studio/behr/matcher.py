from .bahrs import BAHRS


def match_bahr(rukn_sequence):

    best_match = None

    best_score = 0

    for bahr in BAHRS:

        bahr_pattern = bahr["pattern"]

        matches = 0

        total = max(
            len(bahr_pattern),
            len(rukn_sequence)
        )

        for rukn in rukn_sequence:

            if rukn in bahr_pattern:

                matches += 1

        score = (
            matches / total
        ) * 100

        if score > best_score:

            best_score = score

            best_match = bahr["name"]

    return {
        "bahr": best_match,
        "score": round(best_score, 2)
    }