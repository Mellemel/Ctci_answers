def oneAway(old_word: str, new_word: str) -> bool:
    len_old_word = len(old_word)
    len_new_word = len(new_word)
    if abs(len_old_word - len_new_word) > 1:
        return False
    edits = 0
    if len_old_word == len_new_word:
        for i, letter in enumerate(old_word):
            if new_word[i] != letter:
                edits += 1
    elif len_old_word > len_new_word:
        i, j = 0, 0
        while i < len_old_word and j < len_new_word:
            if old_word[i] != new_word[j]:
                edits += 1
                i += 1
            else:
                i += 1
                j += 1
    else:
        i, j = 0, 0
        while i < len_old_word and j < len_new_word:
            if old_word[i] != new_word[j]:
                edits += 1
                j += 1
            else:
                i += 1
                j += 1
    return edits <= 1


data = [
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('paleabc', 'pleabc', True),
    ('pale', 'ble', False),
    ('a', 'b', True),
    ('', 'd', True),
    ('d', 'de', True),
    ('pale', 'pale', True),
    ('pale', 'ple', True),
    ('ple', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False),
    ('pale', 'pse', False),
    ('ples', 'pales', True),
    ('pale', 'pas', False),
    ('pas', 'pale', False),
    ('pale', 'pkle', True),
    ('pkle', 'pable', False),
    ('pal', 'palks', False),
    ('palks', 'pal', False)
]


def test_oneAway():
    for test_s1, test_s2, expected in data:
        assert oneAway(test_s1, test_s2) == expected
