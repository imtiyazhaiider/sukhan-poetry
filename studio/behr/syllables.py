VOWELS = [
    "a",
    "e",
    "i",
    "o",
    "u"
]


def split_syllables(text):

    syllables = []

    current = ""

    for char in text:

        current += char

        if char in VOWELS:

            syllables.append(current)

            current = ""

    if current:

        syllables.append(current)

    return syllables

LONG_VOWELS = [
    "aa",
    "ee",
    "ii",
    "oo",
    "uu",
    "ai",
    "au",
    "ro",
    "ra",
    "re",
    "ri",
    "ru",
]


def syllable_weight(syllable):

    syllable = syllable.lower().strip()

    for vowel in LONG_VOWELS:

        if vowel in syllable:

            return "L"

    vowels = "aeiou"

    vowel_count = sum(
        1
        for char in syllable
        if char in vowels
    )

    if vowel_count >= 2:

        return "L"

    if len(syllable) >= 4:

        return "L"

    return "S"

def split_syllables(text):

    words = text.lower().split()

    syllables = []

    vowels = "aeiou"

    for word in words:

        current = ""

        for i, char in enumerate(word):

            current += char

            next_char = ""

            if i + 1 < len(word):
                next_char = word[i + 1]

            if char in vowels:

                if not next_char or next_char not in vowels:

                    syllables.append(current)

                    current = ""

        if current:

            syllables.append(current)

    return syllables