"""
####  Junction or Self?  ####

In this challenge, you have to separate integers into two families, establishing if they are Junction Numbers or Self Numbers. Given a number n:
___
*) If exists at least a single number which added to the sum of its digits is equal to n, then n is a Junction Number.
*) If there are not numbers which added to the sum of their digits are equal to n, then n is a Self Number.
___

Given a positive integer n, implement a function that returns:
___
*) The string "Self" if n is a Self Number.
*) If n is a Junction Number an array, ordered descendingly, containing the numbers which generate n.
___



[Examples]

___
junction_or_self(25) ➞ [17]
# If we add 17 to the sum of its digits...
# ...17 + 1 + 7 = 25
# 25 is a Junction Number

junction_or_self(818) ➞ [805, 796]
# If we add 805 to the sum of its digits...
# ...805 + 8 + 0 + 5 = 818
# If we add 796 to the sum of its digits...
# ...796 + 7 + 9 + 6 = 818
# 818 is a Junction Number

junction_or_self(7) ➞ "Self"
# 1 + 1 = 2
# 2 + 2 = 4
# 3 + 3 = 6
# No number added to its own digits is equal to 7
# 7 is a Self Number
_____



[Notes]

___
*) As in example #3, the sum of the digits of a positive integer lower than 10 is equal to that same integer.
*) By the formal definition, a Junction number must have at least two other numbers that generate it, so that the Instructions are to be considered valid only for this specific challenge.
*) You can expect only valid data as input.
*) Trivia: the first Junction Number that can be generated by three different numbers is 10000000000001, while the first generated by four different numbers is 1000000000000000000000102.
___



[loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable.
_________
_________
Sum of digits in a string?
https://stackoverflow.com/questions/14550034/sum-of-digits-in-a-string
If i just read my sum_digits function here, it makes sense in my head but it seems to be producing wrong results. Any tip?
_________

"""
#Your code should go here:

