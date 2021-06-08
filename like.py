# testing out different approaches for a candidate 'like' function

from naive_algorithm import naive_algo


# how well does the levenshtein distance perform?
def levenshtein():
    pass


# how well does the damerau-levenshtein distance perform?
def damerau_levenshtein():
    pass


# can we use correlation to test likeness?
def correl():
    pass


# return value 0:1 as a measure of 'likeness' or True (exact match)
# currently using this function as a switch to test out alternative algos
def like(strA, strB, *args):

    if strA == strB:
        return True

    if args:
        result = naive_algo(strA, strB, args[0])

    else:
        result = naive_algo(strA, strB)

    return result


# module test driver function
def main():

    import os

    from read_json_file import read_json_data

    # get test data
    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data = read_json_data(test_data_path)

    param = True
    # param = False

    limit = 0.9

    # run 'like' function against test data
    if data:
        for word_list in data['test_data']:
            for misp in range(1, len(word_list)):
                if param:
                    result = like(word_list[0], word_list[misp], limit)
                else:
                    result = like(word_list[0], word_list[misp])

                print("Is '{}' like '{}'? Result = {}\n".format(word_list[0], word_list[misp], result))
    else:
        print("No data")


# module test
if __name__ == "__main__":
    main()
