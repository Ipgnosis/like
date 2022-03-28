# return the lengths of the strings
def get_lengs(str1, str2):
    """For two strings, return:
        A bool lengths equal/not equal
        Length str 1
        Length str 2
        The shorter of the 2 strings or str1
        The longer of the 2 strings or str2
        """

    len1 = len(str1)
    len2 = len(str2)

    if len1 == len2:
        return (True, len1, len2, str1, str2)
    elif len1 > len2:  # str2 is shorter
        return (False, len2, len1, str2, str1)
    else:  # str1 is shorter
        return (False, len1, len2, str1, str2)
