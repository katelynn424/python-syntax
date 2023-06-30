def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase. """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word uppercased on seperate line if starts with E or e.
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word uppercased on seperate line if starts with one of given letters
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})