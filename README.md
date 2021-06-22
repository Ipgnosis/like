# Python 'Like' function

**This is a work in progress...**

A string compare function that analyzes to what extent string A is similar to string B.

## Background

This idea came from working on a different project where I kept misspelling the country name 'Kazakhstan' as 'Khazakstan'.  I searched for a 'like' function in Python and found none.  This is strange, because this has been implemented in other languages before: there are even 'sounds like' functions (i.e. 'soundex').  So, just for fun, I thought I would give it a shot.  I expect that this will be a lot easier than implementing a spelling checker (or learning how to spell...)

## Ultimate goal

An extension of the Python string object that adds a 'like' operator to test equivalence.  This will enable 'Khazakstan' to match to 'Kazakhstan'.

**Note that this is not a spelling checker.**

The initial implementation will evaluate some kind of probability function.  As a comparison, I will test against the work of [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) and/or [Damerau-Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance).

This will be useful for handling 'typos' resulting from keyboarding errors (e.g. 'typo' vs. 'tyop') that have found their way into data, thereby making it difficult to search upon.

This is *particularly useful* when a string contains international characters that aren't available on all keyboards, for example:

* ñ: the Spanish letter 'eñe'
* ü: the German (etc.) letter u with an umlaut
* ç: the French c-cedilla
* ß: the German letter 'eszett'

(*I suspect that the Cyrillic character set is overly ambitious...*)

Note that the eszett (and others also) is a complication of the general problem in that two letters (i.e. 'ss') can be substituted for the eszett when the keyboard/character set in use doesn’t contain the eszett.  For example: the German word for 'street' is 'straße', which can also be written 'strasse'.

## Implementation

def like(strA, strB, args1 = float)

args1 in range 0 to 1:

* If args[0] then return True (if similarity >= args[0]) or False
* If not args[0] then return float 0:1 - 0 = completely dissimilar; 1 = exact match.

## Test data

The test data (test_data.json) is extracted from a Wikipedia article on the most misspelled words: [Commonly misspelled English words](https://en.wikipedia.org/wiki/Commonly_misspelled_English_words).
