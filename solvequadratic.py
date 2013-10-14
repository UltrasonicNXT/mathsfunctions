import math, mf

class Solvequadratic(mf.Mathsfunction):
    
    def solve(self, a, b, c):

        print str(a)+"x^2 + "+str(b)+"x + "+str(c)

        working = (b*b) - (4*a*c)
        working = math.sqrt(working)
        xa = -b+working
        xb = -b-working
        xa = xa/2*a
        xb = xb/2*a

        if xa == xb:
            return xa
        return xa, xb

    def givehelp(self):
        return "help"

    def liststring(self, a):
        string = ""
        for x in a:
            string += str(x)+" "
        return string

    formats = ('liststring',)

sq = Solvequadratic()
sq.run()
