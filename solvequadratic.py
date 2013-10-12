import math, mf

solvequadratic = mf.Mathsfunction()

def main(a, b, c):

    working = (b*b) - (4*a*c)
    working = math.sqrt(working)
    xa = -b+working
    xb = -b-working
    xa = xa/2*a
    xb = xb/2*a

    print xa
    print xb

def givehelp():
    print "help"

solvequadratic.main = main
solvequadratic.givehelp = givehelp

solvequadratic.run()
