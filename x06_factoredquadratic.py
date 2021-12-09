#!python3
'''
There are a few items to note about the quadratic formula: 
**** The Discriminant The square root part is called the "discriminant".

Depending on the coefficients, it is possible for it to have a negative value. Since you can't square root a negative, when the discrminant is 0, there are no solutions to the equation.
* If the discriminant is 0, there is only 1 solution, because the quadratic is a perfect square
* If the discriminant is positive, there will be 2 solutions
* If the discriminant is a perfect square, then the roots will be rational numbers (fractions) and it is possible to solve the quadratic by factoring rather than having to rely on the quadratic formula
* If the discriminant is not a perfect square, then the roots will be irrational numbers (involving roots) and the quadratic can not be factored.

x06. Determine the factored form
You may use the functions you created in previous assignments
'''

def Factored(a,b,c):
  '''
  input parameters:
  a, b, c: signed float
  These are the coefficients in the quadratic function ax^2 + bx + c = 0
  
  Write the equation in a nicely formatted factored form. This means no fractions
  
  return:
  list : 2 string literals representing the factors.  The order does not matter
  None if the quadratic can not be factored
  '''
  return None

def main():
  assert "(x + 3)" in Factored(1,1,-6) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  main()
  
