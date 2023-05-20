"""
##Shuffle the Name

Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.


[Examples]

___
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"
_____



[Notes]

___
*) There will be exactly one space between the first and last name.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[sorting] [strings]



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.tutorialspoint.com/python/string_split.htm
Returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
_________
_________
join() Method
https://www.tutorialspoint.com/python/string_join.htm
Returns a string in which the string elements of sequence have been joined by str separator.
_________
_________
reversed() Method
https://www.geeksforgeeks.org/python-reversed-function/
Returns an iterator that accesses the given sequence in the reverse order.
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
split() Method
https://www.w3schools.com/jsref/jsref_split.asp#:~:text=The%20split()%20method%20is,is%20split%20between%20each%20character.
Is used to split a string into an array of substrings, and returns the new array. Tip: If an empty string ("") is used as the separator, the string is split between ea …
_________
_________
find() Method
https://www.w3schools.com/python/ref_string_find.asp
Finds the first occurrence of the specified value. Useful for slicing. The find() method returns -1 if the value is not found. The find() method is almost the same as …
_________
_________
Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b,
_________
"""
# Your code should go here:


def nameShuffle(str1):
    lst1 = str1.split(" ")
    reLst1 = [lst1[1], lst1[0]]
    strLst1 = reLst1.join()
    return strLst1

print(nameShuffle("Donald Trump")) # ➞ "Trump Donald"

print(nameShuffle("Rosie O'Donnell")) # ➞ "O'Donnell Rosie"

print(nameShuffle("Seymour Butts")) # ➞ "Butts Seymour"


# testing.
# checkAgain.
# checkAgain. Check all the unknown resources.