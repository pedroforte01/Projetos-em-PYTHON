
def multipicacao (*args):
   total = 1
   for resul in args:
     total *= resul
   return total

resp = multipicacao (1,2,3,4,5)

print (resp)

def P_I(pi):
  if pi % 2 == 0:
    print (pi, "é par!")
  else:
    print (pi, "é impar!")
  return print (pi)


P_I(resp)