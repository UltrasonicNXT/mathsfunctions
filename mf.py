import sys

class Mathsfunction:
    
    def run(self):
        if sys.argv[1] == '--help':
            self.givehelp()
        else:
            args = []
            for arg in sys.argv[1:]:
                args.append(int(arg))
            self.main(*args)
