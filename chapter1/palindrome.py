def isPalimdrome(word: str):
    word = word.lower()
    word_dict = {}
    for letter in word:
        if letter == ' ':
            continue
        if word_dict.get(letter):
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    odd = 0
    for val in word_dict.values():
        if val % 2 != 0:
            odd += 1
    return odd <= 1


data = [
    ('Tact Coa', True),
    ('jhsabckuj ahjsbckj', True),
    ('Able was I ere I saw Elba', True),
    ('So patient a nurse to nurse a patient so', False),
    ('Random Words', False),
    ('Not a Palindrome', False),
    ('no x in nixon', True),
    ('azAZ', True)]

def test_isPalimgdrome():
    for string, expected in data:
        assert isPalimdrome(string) == expected