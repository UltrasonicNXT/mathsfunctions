import sys, inspect

class Mathsfunction:
    
    def run(self):
        inputs = []
        formatas = None;
        inputslen = len(inspect.getargspec(self.solve)[0]) - 1
        for arg in sys.argv[1:]:
            if arg == '--help':
                self.givehelp()
                return
            elif arg.startswith('-format'):
                formatgiven = arg[8:]
                if formatgiven in self.formats:
                    formatas = formatgiven
            else:
                if len(inputs) < inputslen:
                    inputs.append(int(arg))
                else:
                    raise ArguamentsError
                    
        self.result = self.solve(*inputs)

        if not formatas:
            formatas = self.formats[0]

        print getattr(self, formatas)(self.result)

    def error(self, message):
        print message

class ArguamentsError(Exception):
    pass
