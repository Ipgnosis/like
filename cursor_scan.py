# a function to return a score for a set of substring matches between 2 strings

def cursor_scan(str1, str2, cursor, len1):
    """Scan the two strings within specific substrings (cursors) looking for matches
       Return a score for that set of cursors
    """
    cursor_score = 0
    weight = cursor  # we are going to tune this
    i = 0

    while (i + cursor - 1) < len1:
        cursor1 = str1[i: i + cursor]
        if str2.find(cursor1) > -1:
            cursor_score += weight
        i += 1

    return cursor_score


# module test driver function
def main():

    from get_lengs import get_lengs

    # str1 = "Khazakstan"
    # str2 = "Kazakhstan"
    str1 = "amateur"
    str2 = "amature"

    equal_len, len1, len2, strA, strB = get_lengs(str1, str2)

    this_cursor_score = 0
    cursor_count = 0
    new_cursor_score = 0

    for this_cursor in range(2, len1 + 1):

        this_cursor_score = cursor_scan(strA, strB, this_cursor, len1)
        print(f"cursor length = {this_cursor}, cursor_score = {this_cursor_score}")

        cursor_count = (len1 + 1 - this_cursor) * (len2 + 1 - this_cursor)

        if this_cursor_score > 0 and cursor_count > 0:
            new_cursor_score += this_cursor_score / cursor_count
        print(f"cursor_count = {cursor_count}, new_cursor_score = {new_cursor_score}\n")

    print(f"The score for '{strA}' and '{strB}' with cursor {this_cursor} is {new_cursor_score}")


# module test
if __name__ == "__main__":
    main()
