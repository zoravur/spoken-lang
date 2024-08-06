from antlr4 import *
from SpockLexer import SpockLexer
from SpockParser import SpockParser
from SpockListener import SpockListener

class SpockPrintListener(SpockListener):
    def enterEveryRule(self, ctx):
        print(f"Entered {type(ctx).__name__}")

def main(filename):
    # Read the input file
    input_stream = FileStream(filename)
    
    # Create a lexer that feeds off of input stream
    lexer = SpockLexer(input_stream)
    
    # Create a buffer of tokens pulled from the lexer
    stream = CommonTokenStream(lexer)
    
    # Create a parser that feeds off the tokens buffer
    parser = SpockParser(stream)
    
    # Begin parsing at the program rule
    tree = parser.program()
    
    # Create and use a listener
    listener = SpockPrintListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a filename as an argument.")
