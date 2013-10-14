import sys, inspect

class Mathsfunction:
    listinput = None
    
    def run(self):
        inputs = []
        formatas = None;
        inputslen = len(inspect.getargspec(self.solve)[0]) - 1
        for arg in sys.argv[1:]:
            if arg == '--help':
                print self.givehelp()
                return
            elif arg.startswith('-format'):
                formatgiven = arg[8:]
                if formatgiven in self.formats:
                    formatas = formatgiven
            else:
                inputs.append(int(arg))
        if self.listinput:
            self.result = self.solve(inputs)
        else:
            if len(inputs) == inputslen:
                self.result = self.solve(*inputs)
            else:
                raise ArguamentLengthError    

        if not formatas:
            formatas = self.formats[0]

        print getattr(self, formatas)(self.result)

    def error(self, message):
        print message

class ArguamentLengthError(Exception):
    pass

class ArguamentMathsError(Exception):
    pass

def diffs(array):
    return [array[i+1]-x for i,x in enumerate(array[:-1])]

def listequal(array):
    return len(set(array)) == 1
