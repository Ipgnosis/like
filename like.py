# the like code


# return value 0:1 as a measure of 'likeness' or True (exact match)
def like(strA, strB, *args):

    if args:
        threshold = args[0]

    if strA == strB:
        return True

    lenA = len(strA)
    lenB = len(strB)

    # print('lenA = {}, lenB = {}'.format(lenA, lenB))

    tally = 0.0
    incr = 0.1

    if lenA == lenB:
        tally += 0.5

        for posn1 in range(len(strA)):
            if strA[posn1] == strB[posn1]:
                tally += incr

    if args and tally >= threshold:
        return True

    return tally


def main():

    import os
    # from difflib import SequenceMatcher

    from read_json_file import read_json_data

    # str1 = 'Kazakhstan'
    # str2 = 'Khazakstan'

    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data = read_json_data(test_data_path)

    if data:
        for lis in data['test_data']:
            print("{}, {}, {}".format(lis[0], lis[1], like(lis[0], lis[1], 0.9)))

    # no_args = like(str1, str2)

    # with_args = like(str1, str2, 0.9)

    # print('no_args =', no_args)

    # print('with_args =', with_args)


if __name__ == "__main__":
    main()
