# EXAMPLE
# Input: "Mr John Smith  ", 13
# Output: "Mr%20John%20Smith"
def urlify(word : str, length : int) -> str:
    new_word = ''
    for i in range(length):
        if word[i] == ' ':
            new_word += '%20'
        else:
            new_word += word[i]
    return new_word

def test_urlify():
    assert urlify("Mr John Smith  ", 13) == "Mr%20John%20Smith"

def test_urlify_two():
    assert urlify('much ado about nothing      ', 22) == 'much%20ado%20about%20nothing'