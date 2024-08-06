import sys
from antlr4 import InputStream, CommonTokenStream, Token

# import your generated lexer and parser
from SpockLexer import SpockLexer
from SpockParser import SpockParser

def process_chunk(chunk):
    input_stream = InputStream(chunk)
    lexer = SpockLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SpockParser(token_stream)

    token_stream.fill()

    for token in token_stream.tokens:
        if token.type == Token.EOF:
            continue
        # Ensure token type is within the valid range
        if token.type >= 0 and token.type < len(lexer.symbolicNames):
            token_type = lexer.symbolicNames[token.type]
        else:
            token_type = "UNKNOWN"
        print(f'Token: {token.text}, Type: {token_type}')

    # parse the input (this will depend on your grammar's entry point)
    tree = parser.root()  # replace `root` with your actual entry point
    print(tree.toStringTree(recog=parser))

def incremental_parse_from_stdin():
    print("Enter your input (press CTRL+D to finish):")

    buffer = ""

    while True:
        try:
            chunk = sys.stdin.read()
            if not chunk:
                break
            buffer += chunk
            process_chunk(buffer)
            buffer = ""  # clear buffer after processing

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    incremental_parse_from_stdin()

