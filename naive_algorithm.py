# naive algorithm as a baseline

# return the lengths of the strings
def get_lens(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    if len1 == len2:
        lbool = True
    else:
        lbool = False

    return (lbool, len1, len2)


# compile data on upper/lower case incidence in the string
def case_crunching(str1):

    uppers = []
    lowers = []

    for ch in str1:
        if ch.isupper():
            uppers.append(ch)
        else:
            lowers.append(ch)

    print(uppers)
    print(lowers)


# establish a baseline of performance with a naive string matching algorithm
def naive_algo(string1, string2, *args):

    str_len = get_lens(string1, string2)

    tally = 0.0

    avg_len = (str_len[1] + str_len[2]) / 2

    if args:
        incr = 0.1
        threshold = args[0]
        incr = (threshold / avg_len) - incr
    else:
        incr = 1
        incr = incr / avg_len

    if str_len[0]:
        tally += 0.5

        for i in range(len(string1)):
            if string1[i] == string2[i]:
                tally += incr
            elif (i > 0) and (string1[i] == string2[i - 1]):
                tally += incr / 2
            elif (i < str_len[2]) and (string1[i] == string2[i + 1]):
                tally += incr / 2

    else:
        # inequal string lengths results in index error from a 'for' loop
        # need a way to evaluate strings of inequal length
        print('len({}) = {}; len({}) = {}'.format(string1, str_len[1], string2, str_len[2]))

    if args:
        if tally >= threshold:
            return True
        else:
            return False
    else:
        return tally


# module test driver function
def main():

    strA = "Khazakstan"
    strB = "Kazakhstan"

    print(naive_algo(strA, strB))


# module test
if __name__ == "__main__":
    main()
