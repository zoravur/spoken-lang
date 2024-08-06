import sys
import re
from antlr4 import *
from SpockLexer import SpockLexer
from SpockParser import SpockParser
from SpockVisitor import SpockVisitor
from SpockInterpreter import SpockInterpreter

def process_input(interpreter, input_text):
    input_stream = InputStream(input_text)
    lexer = SpockLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpockParser(stream)
    tree = parser.program()

    interpreter.visit(tree)

if __name__ == '__main__':
    interpreter = SpockInterpreter()
    print("Enter your code (type 'exit' to quit):")
    
    buffer = ""
    
    for line in sys.stdin:
        try:
            line = line.replace('\x00', '')
            line = re.sub('[^a-zA-Z0-9 \n]', '', line)
            if line.strip().lower() == 'exit':
                break
            line = ' '.join(line.lower().split()[2:])
            buffer += line + '\n'
            buffer = buffer.lower()
            # print(buffer)
            loc = buffer.find('flush')
            if loc >= 0:
                process_input(interpreter, buffer[:loc])
                buffer = buffer[loc+5:]
                print(buffer)

            # if line.strip().endswith(' flush'):  # Assume statements end with a semicolon
            #     process_input(interpreter, buffer)
            #     buffer = ""  # Clear buffer after processing
        except Exception as e:
            print(f"Error: {e}")

