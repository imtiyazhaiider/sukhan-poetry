RUKN_PATTERNS = {

    ('L','S','L','L'): 'mafailun',

    ('S','L','S','L'): 'failatun',

    ('L','L','S'): 'faulun',

    ('S','L','L'): 'faelun',

    ('S','S','L'): 'mafool',

    ('S','S','L','L'): 'mafoolun',

    ('L','S','S','L'): 'mustafilun',

    ('S','L','L','S'): 'mutafaelun',

    ('L','L','S','L'): 'faailatun',

}

def find_rukn_matches(pattern):

    matches = []

    pattern = tuple(pattern)

    for rukn_pattern, rukn_name in RUKN_PATTERNS.items():

        if pattern[:len(rukn_pattern)] == rukn_pattern:

            matches.append(
                rukn_name
            )

    return matches


def generate_rukn_sequence(pattern):

    results = []

    index = 0

    while index < len(pattern):

        matched = False

        for rukn_pattern, rukn_name in RUKN_PATTERNS.items():

            length = len(rukn_pattern)

            current = tuple(
                pattern[index:index + length]
            )

            if current == rukn_pattern:

                results.append(
                    rukn_name
                )

                index += length

                matched = True

                break

        if not matched:

            results.append("?")

            index += 1

    return results