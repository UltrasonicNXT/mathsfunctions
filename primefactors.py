import math, mf

class Primefactors(mf.Mathsfunction):
    
    def solve(self, a):

        rem = a

        factors = {}
        factors = []
    
        while rem != 1:
            for x in range(2, rem):
                keepthis = True
                while keepthis:
                    if rem%x == 0:
                        rem = rem/x
                        factors.append(x)
                    else:
                        keepthis = False
        return factors

    def givehelp(self):
        return "help"

    def liststring(self, a):
        string = ""
        for x in a:
            string += str(x)+" "
        return string

    def powerstring(self, a):
        string = ""
        factors = {}
        for x in a:
            if x in factors:
                factors[x] += 1
            else:
                factors[x] = 1
                
        first = True  
        for x in factors:
            if not first:
                string+= " x "
            if factors[x] > 1:
                string += str(x)+"^"+str(factors[x])
            else:
                string += str(x)
            first = False
        return string

    formats = ('liststring', 'powerstring')

if __name__ == '__main__':
    pf = Primefactors()
    pf.run()
