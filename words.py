def print_upper_words(words, must_start_with):
    """For a list of words, print words starting with letter in uppercase"""
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                uppercase = word.upper()
                print(uppercase)

print_upper_words(["eagle", "Edward", "Alfred", "zope", "yes"],
                   must_start_with={"A", "E"})