from itertools import count


def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    letter_count = 0
    for let in word:
        if let == letter:
            letter_count += 1
    return letter_count

single_letter_count('Hello World', 'l')
