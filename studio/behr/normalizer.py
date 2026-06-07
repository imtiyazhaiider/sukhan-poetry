import re


def normalize_text(text):

    """
    Convert Urdu, Hindi and Roman Urdu
    into a simplified phonetic form.
    """

    text = text.lower()

    # Urdu characters

    urdu_map = {

        "ا": "a",
        "آ": "aa",
        "ب": "b",
        "پ": "p",
        "ت": "t",
        "ٹ": "t",
        "ث": "s",
        "ج": "j",
        "چ": "ch",
        "ح": "h",
        "خ": "kh",
        "د": "d",
        "ڈ": "d",
        "ذ": "z",
        "ر": "r",
        "ڑ": "r",
        "ز": "z",
        "ژ": "zh",
        "س": "s",
        "ش": "sh",
        "ص": "s",
        "ض": "z",
        "ط": "t",
        "ظ": "z",
        "ع": "",
        "غ": "gh",
        "ف": "f",
        "ق": "q",
        "ک": "k",
        "گ": "g",
        "ل": "l",
        "م": "m",
        "ن": "n",
        "ں": "n",
        "و": "w",
        "ہ": "h",
        "ھ": "h",
        "ء": "",
        "ی": "y",
        "ے": "e",
    }

    # Hindi characters

    hindi_map = {

        "अ": "a",
        "आ": "aa",
        "इ": "i",
        "ई": "ii",
        "उ": "u",
        "ऊ": "uu",
        "ए": "e",
        "ऐ": "ai",
        "ओ": "o",
        "औ": "au",

        "क": "k",
        "ख": "kh",
        "ग": "g",
        "घ": "gh",
        "च": "ch",
        "छ": "chh",
        "ज": "j",
        "झ": "jh",
        "ट": "t",
        "ठ": "th",
        "ड": "d",
        "ढ": "dh",
        "त": "t",
        "थ": "th",
        "द": "d",
        "ध": "dh",
        "न": "n",
        "प": "p",
        "फ": "ph",
        "ब": "b",
        "भ": "bh",
        "म": "m",
        "य": "y",
        "र": "r",
        "ल": "l",
        "व": "v",
        "श": "sh",
        "ष": "sh",
        "स": "s",
        "ह": "h",
    }

    for source, target in urdu_map.items():

        text = text.replace(
            source,
            target
        )

    for source, target in hindi_map.items():

        text = text.replace(
            source,
            target
        )

    text = re.sub(
        r'[^a-z\s]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()