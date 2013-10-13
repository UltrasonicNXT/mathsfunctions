import mf, primefactors

class HCF(mf.Mathsfunction):

    def solve(self, a, b):
        pf = primefactors.Primefactors()

        afactors = pf.solve(a)
        bfactors = pf.solve(b)

        vennmiddle = []

        for x in afactors:
            if x in bfactors:
                vennmiddle.append(x)

        sum = 1
        for x in vennmiddle:
            sum = sum*x

        return sum

    def givehelp(self):
        return "help for HCF"

    def string(self, a):
        return str(a)

    formats = ('string',)

if __name__ == '__main__':
    hcf = HCF()
    hcf.run()
