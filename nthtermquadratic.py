import mf, nthtermlinear

class Nthtermquadratic(mf.Mathsfunction):

    def solve(self, inputs):

        firstdiffs = mf.diffs(inputs)
        seconddiffs = mf.diffs(firstdiffs)

        if not mf.listequal(seconddiffs):
            raise ArguamentMathsError

        a = (seconddiffs[0])/2

        an2 = [a*x*x for x in range(1, 5)]

        array = []

        for i, x in enumerate(an2):
            array.append(inputs[i]-x)

        ntl = nthtermlinear.Nthtermlinear()
        tup = ntl.solve(array)

        return (a, tup[0], tup[1])

    def string(self, ans):
        a = ans[0]
        b = ans[1]
        c = ans[2]

        return str(a)+"n^2 + "+str(b)+" + "+str(c)

    formats = ('string',)

    listinput = True

if __name__ == '__main__':
    ntq = Nthtermquadratic()
    ntq.run()
        
            
