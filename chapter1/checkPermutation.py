def isPermutation(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    word_one = word_one.lower()
    word_two = word_two.lower()
    letters_one = {}
    letters_two = {}
    for letters in word_one:
        if (letters_one.get(letters)):
            letters_one[letters] += 1
        else:
            letters_one[letters] = 1
    for letters in word_two:
        if (letters_two.get(letters)):
            letters_two[letters] += 1
        else:
            letters_two[letters] = 1
    keys_one = letters_one.keys()
    keys_two = letters_two.keys()
    if set(keys_one) != set(keys_two):
        return False
    for key in letters_one.keys():
        if letters_one[key] != letters_two[key]:
            return False
    return True

def test_isPermutation_different_lengths():
    assert isPermutation('hello', 'melvin') == False

def test_isPermutation_different_():
    assert isPermutation('hello', 'world') == False

def test_isPermutation_same():
    assert isPermutation('hello', 'olleh') == True

def test_isPermutation_case_insensitive():
    assert isPermutation('Hello', 'hello') == True