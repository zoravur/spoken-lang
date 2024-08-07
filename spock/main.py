import sys
import re
import argparse
from antlr4 import *
from gen.SpockLexer import SpockLexer
from gen.SpockParser import SpockParser
from SpockInterpreter import SpockInterpreter

def process_input(interpreter, input_text):
    input_stream = InputStream(input_text)
    lexer = SpockLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpockParser(stream)
    tree = parser.program()

    interpreter.visit(tree)


def preprocess_line(line):
    # Necessary because the script for the audio input has a strange format.
    # The input format can be seen by running `arecord -f S16_LE -c1 -r 16000 -t raw -D default | nc localhost {PORT}`
    # Along with whisper_streaming/whisper_online_server.py
    line = line.replace('\x00', '')
    line = re.sub('[^a-zA-Z0-9 \n]', '', line)
    line = ' '.join(line.lower().split()[2:])
    return line


def interpret_live(interpreter):
    interpreter = SpockInterpreter()
    
    buffer = ""
    
    for line in sys.stdin:
        try:
            line = preprocess_line(line)
            buffer += line + '\n'
            buffer = buffer.lower()
            # print(buffer)
            loc = buffer.find('flush')
            if loc >= 0:
                sys.stderr.write(buffer[:loc] + '\n')
                process_input(interpreter, buffer[:loc])
                buffer = buffer[loc+5:]
        except Exception as e:
            print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Spock interpreter")
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, help="Input file")
    args = parser.parse_args()

    interpreter = SpockInterpreter()

    if args.input_file == sys.stdin:
        interpret_live(interpreter)
        return
    
    if not args.input_file.name.endswith('.spk'):
        print("Error: Invalid file extension. Spock files should have a .spk extension")
        return
    
    with args.input_file as f:
        process_input(interpreter, f.read())

if __name__ == '__main__':
    main()