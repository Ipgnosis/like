# count characters in same position between two strings


from naive_algorithm import get_lens


def char_overlap(string1, string2):

    sort1 = "".join(sorted(string1))
    sort2 = "".join(sorted(string2))

    if sort1 == sort2:
        return 1
    else:
        return 0


# a common substring is defined as two (or more) consecutve characters that appear in both strings
def count_chars(string1, string2):

    substr_list = []
    count = 0

    # evaluate the string lengths
    lens = get_lens(string1, string2)

    # if the strings are of unequal length, make string1 the longer string
    if (not lens[0]) and (lens[2] > lens[1]):
        tempstr = string1
        string1 = string2
        string2 = tempstr

    # if strings of equal length
    if lens[0]:
        # traverse the strings
        for i in range(len(string1)):
            if string1[i] == string2[i]:
                count += 1
    else:
        j = 0
        for i in range(len(string1)):
            if string1[i] == string2[j]:
                count += 1
                j += 1
            else:
                pass




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
