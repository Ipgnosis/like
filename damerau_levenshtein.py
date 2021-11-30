
#  implements Damerau-Levenshtein algo for measuring the edit distance between two strings

def damerau_levenshtein(a, b):
    '''Returns an integer indicating the number of insertions, substitutions or transpositions separating str a and str b'''

    # a = car
    # b = cat
    lenA = len(a)
    lenB = len(b)
    maxdist = lenA + lenB

    Σ = 26

    listA = []
    listB = []
    da = []  # alphabet length

    for i in range(1, Σ + 1):  # 1 to |Σ| # inclusive do
        da[i] = 0
    # da = [0, 0, 0]

    for j in range(-1, lenA, 1):
        listA[j] = 0
    # listA = [0, 0, 0, 0]

    for k in range(-1, lenB, 1):
        listB[k] = 0
    # listB = [0, 0, 0, 0]

    d = [listA, listB]  # a 2-d array of integers, dimensions length(a)+2, length(b)+2
    # note that d has indices starting at −1, while a, b and da are one-indexed.
    # d = [[0, 0, 0, 0], [0, 0, 0, 0]]

    d[−1][−1] = maxdist

    for l in range(0, lenA):  # inclusive do
        d[l][−1] = maxdist
        d[l][0] = l

    for m in range(0, lenB):  # inclusive do
        d[−1][m] = maxdist
        d[0][m] = m

    for r in range(1, lenA)  # inclusive do
        db = 0
        for s in range(1, lenB)  # inclusive do
            k = da[b][s]
            ℓ = db

            if a[r] == b[s]:
                cost = 0
                db = s
            else:
                cost = 1

            d[r][s] = minimum(d[r−1][s−1] + cost,  # substitution
                               d[r][s−1] + 1,    # insertion
                               d[r−1][s] + 1,    # deletion
                               d[k−1][ℓ−1] + (r−k−1) + 1 + (s-ℓ−1))  # transposition

        da[a][r] = r  ### huh? ###

    return d[lenA][lenB]


#  invoke damerau_levenshtein
def main():
    str1 = 'Kazakhstan'
    str2 = 'Khazakstan'

    result = damerau_levenshtein(str1, str2)
    print(result)


# stand-alone test invocation
if __name__ == "__main__":
    main()


#  pseudo-code
#  convert to Python 3
"""
algorithm DL-distance is
    input: strings a[1..length(a)], b[1..length(b)]
    output: distance, integer

    da := new array of |Σ| integers
    for i := 1 to |Σ| inclusive do
        da[i] := 0

    let d[−1..length(a), −1..length(b)] be a 2-d array of integers, dimensions length(a)+2, length(b)+2
    // note that d has indices starting at −1, while a, b and da are one-indexed.

    maxdist := length(a) + length(b)
    d[−1, −1] := maxdist
    for i := 0 to length(a) inclusive do
        d[i, −1] := maxdist
        d[i, 0] := i
    for j := 0 to length(b) inclusive do
        d[−1, j] := maxdist
        d[0, j] := j

    for i := 1 to length(a) inclusive do
        db := 0
        for j := 1 to length(b) inclusive do
            k := da[b[j]]
            ℓ := db
            if a[i] = b[j] then
                cost := 0
                db := j
            else
                cost := 1
            d[i, j] := minimum(d[i−1, j−1] + cost,  //substitution
                               d[i,   j−1] + 1,     //insertion
                               d[i−1, j  ] + 1,     //deletion
                               d[k−1, ℓ−1] + (i−k−1) + 1 + (j-ℓ−1)) //transposition
        da[a[i]] := i
    return d[length(a), length(b)]

    """
