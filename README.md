# Python Like

A work in progress...

A string compare function that analyzes to what extent strA is similar to strB.

## Ultimate goal

An extension of the string object that adds a 'like' operator to test equivalence.  This will enable 'Khazakstan' to match to 'Kazakhstan'.

**Note that this is not a spelling checker.**

The implementation is almost certainly on some kind of probability function.

Useful for 'typos' resulting from keyboarding errors, such as 'typo' vs. 'tyop' that haven't been caught by a spelling checker.

This is particularly useful when a string contains international characters (that aren't available on all keyboards), such as:

	• ñ: the Spanish letter 'eñe'
	• ü: the German (etc.) letter u with an umlaut
	• ß: the German letter 'eszett'

Note that the eszett (and maybe others also) is a complication of the general problem in that two letters 'ss' are substituted for the eszett when the character set in use doesn’t contain the eszett.  For example: the German word for 'street' is 'straße' which can also be written 'strasse'.

Extra credit for 'soundslike()', which would be really cool…

## Implementation

def like(strA, strB, args1 = float)

args1 in range 0 to 1:

* If args[0] then return True or False if similarity >= args[0]
* If not args then return float 0:1 - 0 = completely dis similar; 1 = exact match.


## Test data

The test data (test_data.json) is extracted from a Wikipedia article on the most misspelled words: [Commonly misspelled English words](https://en.wikipedia.org/wiki/Commonly_misspelled_English_words).
