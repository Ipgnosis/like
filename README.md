# Python Like

A work in progress...

A string compare function that analyzes to what extent strA is similar to strB.

def like(strA, strB, args1 = float)

args1 in range 0 to 1:

* If args[0] then return True or False if similarity >= args[0]
* If not args then return float 0:1 - 0 = completely dis similar; 1 = exact match.
