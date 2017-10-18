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
    #print(tree.toStringTree(recog=parser))

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

def report(argv, nb_requests = 10):
    i = 0
    nb_join = 0
    nb_transac = 0

    with open(argv[1], 'r') as file:
        for line in file:
            tree = SqlParser(CommonTokenStream(SqlLexer(InputStream(line)))).sql_stmt()
            walker = ParseTreeWalker()
            metrics = Metrics()
            walker.walk(metrics, tree)

            nb_join += metrics.howManyJoins()
            nb_transac += metrics.howManyTransactions()
            
            i += 1
            if i >= nb_requests:
                break

    print(nb_requests, "requests have been analysed")
    print("Overall, there are")
    print(" -", nb_join, "joins")
    print(" -", nb_transac, "transactions")
    ## end

if __name__ == '__main__':
    #main(sys.argv)
    report(sys.argv, 5)