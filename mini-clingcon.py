import sys
from clingo.application import clingo_main, Application
from clingo.script import enable_python

enable_python()

class MiniClingconApp(Application):

    program_name = "mini-clingcon"
    version = "1.0"
    
    def main(self, ctl, files):
        for path in files:
            ctl.load(path)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()

if __name__ == "__main__":
    clingo_main(MiniClingconApp(), sys.argv[1:])
