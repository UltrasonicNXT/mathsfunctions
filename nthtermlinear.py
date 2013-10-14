import mf

class Nthtermlinear(mf.Mathsfunction):

    def solve(self, inputs):

        diffs = mf.diffs(inputs)

        if not mf.listequal(diffs):
            raise mf.ArguamentMathsError

        a = diffs[0]
        b = inputs[0]-diffs[0]

        return (a, b)

    def string(self, ans):
        a = ans[0]
        b = ans[1]

        return str(a)+"n + "+str(b)

    formats = ('string',)

    listinput = True

if __name__ == '__main__':
    ntl = Nthtermlinear()
    ntl.run()
        
            
