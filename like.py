# testing out different approaches for a candidate 'like' function

# from naive_algorithm import naive_algo
from get_lengs import get_lengs
from cursor_scan import cursor_run


# how well does the levenshtein distance perform?
def levenshtein():
    pass


# how well does the damerau-levenshtein distance perform?
def damerau_levenshtein():
    pass


# return value 0:1 as a measure of 'likeness' or True (exact match)
# currently using this function as a switch to test out alternative algos
def like(str1, str2, *args):

    if str1 == str2:  # if A matches B, we are done
        return True

    equal_len, len1, len2, strA, strB = get_lengs(str1, str2)

    result = 0

    if args:  # if a limit has been provided, send it
        # result = naive_algo(strA, strB, args[0])
        pass

    else:
        # result = naive_algo(strA, strB)
        for this_cursor in range(2, len1 + 1):
            result = cursor_run(strA, strB, len1, len2)

    return result


# module test driver function
def main():

    import os

    from read_json_file import read_json_data

    # get test data
    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data_file = read_json_data(test_data_path)

    # Send limit or not??
    # param = True
    param = False

    limit = 0.9

    # run 'like' function against test data
    if data_file:
        for word_list in data_file['test_data']:
            for misp in range(1, len(word_list)):
                if param:
                    result = like(word_list[0], word_list[misp], limit)
                else:
                    result = like(word_list[0], word_list[misp])

                print(f"'{word_list[0]}' cf. '{word_list[misp]}'? Result = {result}")
    else:
        print("No data")


# module test
if __name__ == "__main__":
    main()
