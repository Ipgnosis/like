# naive algorithm as a baseline

from get_lengs import get_lengs


# compile data on upper/lower case incidence in the string
def case_crunching(str1):
    """Compile data on upper/lower case incidence in the string"""

    uppers = []
    lowers = []
    upper_count = 0
    lower_count = 0

    for ch in str1:
        if ch.isupper():
            uppers.append(ch)
            upper_count += 1
        else:
            lowers.append(ch)
            lower_count += 1

    print(f"Upper case chars: {uppers}")
    print(f"Lower case chars: {lowers}")

    return (upper_count, lower_count)


# can we use correlation to test likeness?
def correl(str1, str2):

    equal_len, len1, len2, strA, strB = get_lengs(sorted(str1), sorted(str2))

    if equal_len:
        pass


# establish a baseline of performance with a naive string matching algorithm
def naive_algo(string1, string2, *args):
    """Establish a baseline of performance with a naive string matching algorithm"""

    # test the lengths and get the shorter string back first
    equal_len, len1, len2, strA, strB = get_lengs(string1, string2)
    prior_equivalence = True  # whether the last string comparison succeeded or not
    tally = 0.0

    if not equal_len:
        tally = len2 - len1  # start the tally off at the difference between the 2 lengths

    avg_len = (len1 + len2) / 2  # ??

    if args:
        incr = 0.1
        threshold = args[0]  # the limit below which returns false
        incr = (threshold / avg_len) - incr  # ??
    else:
        incr = 1
        # incr = incr / avg_len  # ??

    for i, char in enumerate(strA):  # iterate over the shorter string
        if char == strB[i]:  # if chars are equal
            tally += incr
            prior_equivalence = True
        elif prior_equivalence:
            if (i < len2 - 1) and (char == strB[i + 1]):
                tally += incr / 2  # give a half point for a transposition
                prior_equivalence = False
        else:  # the chars are unequal and the last pair was unequal
            if (char == strB[i - 1]):
                tally += incr / 2  # give a half point for a transposition
                prior_equivalence = False

    if args:
        if tally >= threshold:
            return True
        else:
            return False
    else:
        return tally / len2


# module test driver function
def main():

    strA = "Khazakstan"
    strB = "Kazakhstan"
    strA = "amateur"
    strB = "amature"

    print(f"The difference between '{strA}' and '{strB}' is {naive_algo(strA, strB)}")


# module test
if __name__ == "__main__":
    main()
