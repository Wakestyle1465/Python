from operator import truediv


def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for list in lst:
        if list.type == list:
            return True
        else:
            return False