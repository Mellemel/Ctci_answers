def isUnique(word):
    word = word.lower()
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True

def test_isUnique_true():
    assert isUnique("love") == True

def test_isUnique_false():
    assert isUnique("moon") == False