"""
##Add, Subtract, Multiply or Divide?

Write a function that takes two numbers and returns if they should be added,
subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.


[Examples]

___
operation(15, 9) ➞ "added"

operation(26, 2) ➞ "subtracted"

operation(11, 11) ➞ None
_____



[Notes]

___
*) Only integers are used as test input.
*) Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
*) The function should return either "added", "subtracted", "divided", "multiplied" or None.
___



[math] [numbers]



-------------------------------------------------------------------
[Resources]
_________
get() Method
https://www.programiz.com/python-programming/methods/dictionary/get
You can create a dictionary ended with .get() module to find which operator used to reach intended value.
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b,
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=SKR-8fowFiE
In this video, you will learn how to solve these problems: 0:22 Return a String as an Integer, 1:31 Add, Subtract, Multiply or Divide?, 4:35 To the Power of ___...
_________
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
_________
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
"""
# Your code should go here:


def operation(num1, num2):
    if num1 + num2 == 24:
        return "added"
    elif num1 - num2 == 24:
        return "subsracted"
    elif num1 * num2 == 24:
        return "multiplied"
    elif num1 / num2 == 24:
        return "divided"
    else:
        return None


print(operations(15, 9)) # ➞ "added"
print(operations(26, 2))  # ➞ "subtracted"
print(operations(11, 11)) # ➞ None


# testing.