import sys
from antlr4 import *
from parser.SqlLexer import SqlLexer
from parser.SqlParser import SqlParser
from parser.SqlListener import SqlListener
from Metrics import Metrics

def parse(query):
    lexer = SqlLexer(InputStream(query))
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    #parser.buildParseTrees = False
    tree = parser.sql_stmt()
    if parser._syntaxErrors > 0:
        print(tree.toStringTree(recog=parser))
        print("There are",parser._syntaxErrors,"syntax errors here")
    return parser._syntaxErrors

def main(argv):
    i = 0
    nbErr = 0
    with open(argv[1], 'r') as file:
        for i, line in enumerate(file):
            nbErr += parse(line)
            if nbErr > 0:
                break
    print(nbErr,"syntax errors found")

if __name__ == '__main__':
    main(sys.argv)