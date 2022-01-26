#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''

import x05_roots
import math


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
  roots = x05_roots.roots(a,b,c)
  if roots == None:
    return None
  roota = abs(roots[0])
  rootb = abs(roots[1])

  if roots[0] > 0 :
    porma = "-"
  else:
    porma = "+"

  if roots[1] > 0 :
    pormb = "-"
  else:
    pormb = "+"


  lista = [a*1,a*roota]
  listb = [a*1,a*rootb]
  
  da =  math.gcd(a*1,int(a*roota))
  db =  math.gcd(a*1,int(a*rootb))

  lista = [int(a/da),int(a*roota/da)]
  listb = [int(a/db),int(a*rootb/db)]

  if lista[0] == 1:
    lista[0] = ""
  if listb[0] == 1:
    listb[0] = ""
  
  re = [f"({lista[0]}x {porma} {lista[1]})",f"({listb[0]}x {pormb} {listb[1]})"]


  # (qx+w)(ex+r)    b = qr + ew    a = qe    c = wr
  




  return re









def main():
  assert ("(x + 3)" in Factored(1,1,-6)) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert "(3x + 1)" in Factored(6,-7,-3) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  main()
  
