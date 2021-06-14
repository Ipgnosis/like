# Python3 program to sort letters
# of string alphabetically

from itertools import accumulate
from functools import reduce


# Python3 program to sort letters
# of string alphabetically
def sortString1(str):
    return "".join(sorted(str))


# Python3 program to sort letters
# of string alphabetically
def sortString2(str):
    return tuple(accumulate(sorted(str)))[-1]


# Python3 program to sort letters
# of string alphabetically
def sortString3(str):
    return reduce(lambda a, b: a + b, sorted(str))


# Python3 program to sort letters
# of string alphabetically in different cases
def sortString4(str):
    return "".join(sorted(str, key=lambda x: x.lower()))


# module test driver function
def main():
    import os
    import time

    from read_json_file import read_json_data

    # get test data
    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data = read_json_data(test_data_path)

    time1 = time2 = time3 = time4 = 0.0

    # run 4 sortString functions against test data
    if data:
        start = end = 0.0
        count = 0
        start = time.time()
        for word_list in data['test_data']:
            for word in word_list:
                results = sortString1(word)
                count += 1
        # end = time.time()
        # time1 = end - start

        # start = end = 0.0
        count = 0
        # start = time.time()
        for word_list in data['test_data']:
            for word in word_list:
                results = sortString1(word)
                count += 1
        # end = time.time()
        # time2 = end - start

        # start = end = 0.0
        count = 0
        # start = time.time()
        for word_list in data['test_data']:
            for word in word_list:
                results = sortString1(word)
                count += 1
        # end = time.time()
        # time3 = end - start

        # start = end = 0.0
        count = 0
        # start = time.time()
        for word_list in data['test_data']:
            for word in word_list:
                results = sortString1(word)
                count += 1
        end = time.time()
        time4 = end - start

    else:
        print("No data")

    print("Words tested = ", count)
    print("sortString1 took: {} seconds\n".format(round(time4, 10))),
    # print("sortString2 took: {} seconds\n".format(round(time2, 10))),
    # print("sortString3 took: {} seconds\n".format(round(time3, 10))),
    # print("sortString4 took: {} seconds\n".format(round(time4, 10))),


def xmain():

    str1 = "seize"
    str2 = "sieze"
    # Result = ze

    results = sortString1(str1, str2)

    print("\nTest = {}, {}".format(str1, str2))
    for result in results:
        print("Result = {}".format(result))


# module test
if __name__ == "__main__":
    main()
