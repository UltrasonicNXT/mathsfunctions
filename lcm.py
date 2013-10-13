import mf, primefactors

class LCM(mf.Mathsfunction):

    def solve(self, a, b):
        pf = primefactors.Primefactors()

        afactors = pf.solve(a)
        bfactors = pf.solve(b)

        venna = []
        vennb = []
        vennmiddle = []

        for x in afactors:
            if x in bfactors:
                vennmiddle.append(x)
                bfactors.remove(x)
            else:
                venna.append(x)
        vennb = bfactors

        allfactors = venna + vennmiddle + vennb

        sum = 1
        for x in allfactors:
            sum = sum*x

        return sum

    def givehelp(self):
        return "help for LCM"

    def string(self, a):
        return str(a)

    formats = ('string',)

if __name__ == '__main__':
    lcm = LCM()
    lcm.run()
