"""
####  Persistence  ####

If you take an integer and form the product of its individual digits, you get a smaller number. Keep doing this and eventually you end up with a single digit.
The number of steps it takes to reach this point is known as the integer's multiplicative persistence. For example, 347 has a persistence of 3: 3*4*7 = 84, 8*4 = 32, 3*2 = 6.
Devise a function that returns the persistence of an integer.


[Examples]

___
persistence(9) ➞ 0

persistence(12) ➞ 1

persistence(6788) ➞ 6

persistence(678852) ➞ 2
_____



[Notes]

___
*) The smallest number with persistence 11 is 277777788888899.
*) A number has never been found, no matter how large, that has a persistence greater than 11.
___



[math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
MultiplicativePersistence
https://github.com/anomen-s/programming-challenges/blob/master/coderbyte.com/easy/Multiplicative%20Persistence/solve.py
Using the Python language, have the function MultiplicativePersistence(num) take the num parameter being passed which will always be a positive integer and return its …
_________

"""
#Your code should go here:

