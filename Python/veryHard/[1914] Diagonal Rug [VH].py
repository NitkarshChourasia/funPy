"""
####  Diagonal Rug  ####

Create a function that takes in size and direction and generates a diagonal rug.
The size is the n parameter, and all rugs are square n x n. The direction is whether the diagonal part begins on the left or the right side.


[Examples]

___
generate_rug(4, "left") ➞ [
  [0, 1, 2, 3],
  [1, 0, 1, 2],
  [2, 1, 0, 1],
  [3, 2, 1, 0]
]

generate_rug(5, "right") ➞ [
  [4, 3, 2, 1, 0],
  [3, 2, 1, 0, 1],
  [2, 1, 0, 1, 2],
  [1, 0, 1, 2, 3],
  [0, 1, 2, 3, 4]
]

generate_rug(1, "left") ➞ [
  [0]
]

generate_rug(2, "right") ➞ [
  [1, 0],
  [0, 1]
]
_____



[Notes]

___
*) n > 0
*) A 1 x 1 rug is trivially [[0]] (same for left and right).
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
slice() Method
https://www.programiz.com/python-programming/methods/built-in/slice
Returns a slice object that is used to slice any sequence (string, tuple, list, range, or bytes).
_________

"""
#Your code should go here:

