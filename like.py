# the like code


# return value 0:1 as a measure of 'likeness' or True (exact match)
def like(strA, strB, *args):

    if args:
        threshold = args[0]

    if strA == strB:
        return True

    lenA = len(strA)
    lenB = len(strB)

    tally = 0.0
    incr = 0.1

    if lenA == lenB:
        tally += 0.5

        for posn1 in range(len(strA)):
            if strA[posn1] == strB[posn1]:
                tally += incr
    else:
        # inequal string lengths results in index error from a for loop
        # need a way to evaluate strings of inequal length
        print('len({}) = {}; len({}) = {}'.format(strA, lenA, strB, lenB))

    if args:
        if tally >= threshold:
            return True
        else:
            return False
    else:
        return tally


def main():

    import os
    # from difflib import SequenceMatcher

    from read_json_file import read_json_data

    # str1 = 'Kazakhstan'
    # str2 = 'Khazakstan'
    # no_args = like(str1, str2)
    # with_args = like(str1, str2, 0.9)
    # print('no_args =', no_args)
    # print('with_args =', with_args)

    # get test data
    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data = read_json_data(test_data_path)

    # run function like against test data
    if data:
        for lis in data['test_data']:
            print("{}, {}, {}".format(lis[0], lis[1], like(lis[0], lis[1], 0.9)))


if __name__ == "__main__":
    main()
