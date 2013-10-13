import math, mf

class Primefactors(mf.Mathsfunction):
    
    def solve(self, a):

        rem = a

        factors = {}
    
        while rem != 1:
            for x in range(2, rem):
                keepthis = True
                while keepthis:
                    if rem%x == 0:
                        rem = rem/x
                        if x in factors:
                            factors[x] += 1
                        else:
                            factors[x] = 1

                    
                    else:
                        keepthis = False
        return factors

    def givehelp(self):
        print "help"

    def liststring(self, a):
        string = ""
        for x in a:
            string += str(x)+" "
        return string

    def powerstring(self, a):
        string = ""
        first = True  
        for x in a:
            if not first:
                string+= " x "
            if a[x] > 1:
                string += str(x)+"^"+str(a[x])
            else:
                string += str(x)
            first = False
        return string

    formats = ('liststring', 'powerstring')

primefactors = Primefactors()
primefactors.run()
