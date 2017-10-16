import sys
from antlr4 import *
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from SqlListener import SqlListener

def main(argv):
    input = FileStream(argv[1])
    lexer = SqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.sql_stmt()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)