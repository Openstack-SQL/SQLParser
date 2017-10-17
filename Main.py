import sys
from antlr4 import *
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from SqlListener import SqlListener
from Metrics import Metrics

def parse(query):
    print(query)
    lexer = SqlLexer(InputStream(query))
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.sql_stmt()
    # print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()
    metrics = Metrics()
    walker.walk(metrics, tree)
    print("There are", metrics.howManyJoins(), "joins")
    print("There are", metrics.howManyTransactions(), "transactions")

def main(argv):
    i = 0
    with open(argv[1], 'r') as file:
        for line in file:
            parse(line)
            i += 1
            if i > 10:
                break

if __name__ == '__main__':
    main(sys.argv)