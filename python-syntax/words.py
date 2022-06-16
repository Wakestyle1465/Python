def print_upper_words(list,must_start_with):
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], 'h')