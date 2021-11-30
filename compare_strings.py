def compare_length(strA, strB):

    '''Compare the length of 2 strings and return a float'''

    return float(len(strA) / len(strB))


def compare_contents(strA, strB):
    '''Compare the commonality of the characters in the 2 strings'''

    print(sorted(strA.lower()))
    print(sorted(strB.lower()))

    rel_length = compare_length(strA, strB)

    if rel_length != 1:
        if rel_length > 1:
            for i in range(len(strA) - len(strB)):
                strB = strB + ' '
        else:
            for i in range(len(strB) - len(strA)):
                strA = strA + ' '

    print('#{}#'.format(strA))
    print('#{}#'.format(strB))



# stand-alone test code
def main():
    str1 = "cat"
    str2 = "bat"
    str3 = "caterpillar"

    print("Length comparison:", compare_length(str1, str3))
    print("Contents comparison:", compare_contents(str1, str3))


# invoke stand-alone test
if __name__ == "__main__":
    main()
