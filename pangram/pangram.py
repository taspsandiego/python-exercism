def is_pangram(sentence=""):
    # Make sure sentence is in lowercase
    sentence = sentence.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    total = len(alphabet)
    for letter in alphabet:
        lookupletter = sentence.find(letter)
        if lookupletter == -1:
            total += lookupletter

    if total == 26:
        return True
    else:
        return False
    
