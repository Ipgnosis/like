# detect common substrings between two strings

# a common substring is defined as two (or more) consecutve characters that appear in both strings
def common_substr(string1, string2):

    substr_list = []

    # traverse first string trailing char
    for i in range(len(string1)):
        candidate_str = ""
        caught = False

        # traverse first string leading char
        for j in range(len(string1) + 1):
            this_str = string1[i: j]

            # if the substring > single char and is found in second string
            if (len(this_str) > 1) and (this_str in string2):

                # check we havent already found this substring
                if (len(candidate_str) == 0) or (candidate_str in this_str):
                    candidate_str = this_str

        # if we have a candidate string and we also have a substring entry
        if (len(candidate_str) > 0) and (len(substr_list) > 0):
            # check we haven't already found this substring
            for substr in substr_list:
                if candidate_str in substr:
                    caught = True
                    break

        # if this is a unique substring, append to substr_list
        if not caught and (len(candidate_str) > 0):
            substr_list.append(candidate_str)

    # search for dups
    dup_candidates = []
    for s in range(len(substr_list)):
        for t in range(len(substr_list)):
            if (substr_list[s] in substr_list[t]) and (s != t):
                dup_candidates.append(substr_list[s])

    # delete the dups
    for p in dup_candidates:
        substr_list.remove(p)

    return substr_list


# module test driver function
def main():
    import os

    from read_json_file import read_json_data

    # get test data
    test_data = "test_data.json"
    CURRENT_DIR_STR = os.path.abspath('')
    test_data_path = os.path.join(CURRENT_DIR_STR, 'data', test_data)

    data = read_json_data(test_data_path)

    # run 'common_substr' function against test data
    if data:
        for word_list in data['test_data']:
            for misp in range(1, len(word_list)):
                results = common_substr(word_list[0], word_list[misp])
                print("\nTest = {}, {}".format(word_list[0], word_list[misp]))
                for result in results:
                    print("Result = {}".format(result))
    else:
        print("No data")


def xmain():

    str1 = "seize"
    str2 = "sieze"
    # Result = ze

    results = common_substr(str1, str2)

    print("\nTest = {}, {}".format(str1, str2))
    for result in results:
        print("Result = {}".format(result))


# module test
if __name__ == "__main__":
    main()
