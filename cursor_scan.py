# a function to return a score for a set of substring matches between 2 strings

def cursor_scan(str1, str2, cursor, len1):
    """Scan the two strings within specific substrings (cursors) looking for matches
       Return a score for that set of cursors
    """
    cursor_score = 0
    weight = cursor  # we are going to tune this
    i = 0

    while (i + cursor - 1) < len1:
        next_cursor = str1[i: i + cursor]
        if str2.find(next_cursor) > -1:
            cursor_score += cursor * weight
        i += 1

    return cursor_score


# cursor run generator
def cursor_run(loc_strA, loc_strB, loc_len1, loc_len2):

    this_cursor_score = 0
    cursor_count = 0
    tot_cursor_score = 0

    for this_cursor in range(2, loc_len1 + 1):

        new_cursor_score = 0

        this_cursor_score = cursor_scan(loc_strA, loc_strB, this_cursor, loc_len1)
        # print(f"cursor length = {this_cursor}, cursor_score = {this_cursor_score}")

        cursor_count = (loc_len1 + 1 - this_cursor) * (loc_len2 + 1 - this_cursor)

        if this_cursor_score > 0 and cursor_count > 0:
            new_cursor_score = this_cursor_score / cursor_count
            tot_cursor_score += new_cursor_score
        # print(f"cursor_count = {cursor_count}, new_cursor_score = {new_cursor_score}, tot_cursor_score = {tot_cursor_score}\n")

    return tot_cursor_score


# module test driver function
def main():

    from get_lengs import get_lengs

    # str1 = "Khazakstan"
    # str2 = "Kazakhstan"
    str1 = "amateur"
    str2 = "amature"

    equal_len, this_len1, this_len2, this_strA, this_strB = get_lengs(str1, str2)

    # cursor_run_score = cursor_scan(this_strA, this_strB, 3, this_len1)
    cursor_run_score = cursor_run(this_strA, this_strB, this_len1, this_len2)

    print(f"The score for '{this_strA}' and '{this_strB}' is {cursor_run_score}")


# module test
if __name__ == "__main__":
    main()
