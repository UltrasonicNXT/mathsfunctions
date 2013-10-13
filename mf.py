import sys, inspect

class Mathsfunction:
    
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
              
        if len(inputs) == inputslen:  
            self.result = self.solve(*inputs)
        else:
            raise ArguamentsError    

        if not formatas:
            formatas = self.formats[0]

        print getattr(self, formatas)(self.result)

    def error(self, message):
        print message

class ArguamentsError(Exception):
    pass
