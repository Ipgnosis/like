# naive algorithm as a baseline

from naive_algorithm import get_lens


# detect matching substrings between two strings
# a matching substring is defined as two (or more) consecutve characters that appear in both strings
def get_substr(string1, string2):

    str_len = get_lens(string1, string2)

    substrings = []

    if str_len[0]:

        for i in range(len(string1)):
            this_substring1 = []
            if string1[i] == string2[i]:
                this_substring1.append(string1[i])
                get_substr(string1[i + 1:], string2[i + 1:])

        substrings.append(this_substring1)

    return substrings


# module test driver function
def main():

    strA = "Khazakstan"
    strB = "Kazakhstan"

    print(get_substr(strA, strB))


# module test
if __name__ == "__main__":
    main()
