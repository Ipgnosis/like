# the like code

def like(strA, strB, *args):

	if args:
		threshold = args[0]

	if strA == strB:
		return True

	lenA = len(strA)
	lenB = len(strB)

	print('lenA = {}, lenB = {}'.format(lenA, lenB))

	tally = 0.0
	incr = 0.1

	if lenA == lenB:
		tally = 0.5

	for posn1 in range(len(strA)):
		if strA[posn1] == strB[posn1]:
			tally += incr

	if args and tally >= threshold:
		return True

	return tally


def main():
	str1 = 'Kazakhstan'
	str2 = 'Khazakstan'

	no_args = like(str1, str2)

	with_args = like(str1, str2, 0.9)

	print('no_args =', no_args)

	print('with_args =', with_args)

if __name__ == "__main__":
	main()
