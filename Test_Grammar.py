import sys
import time
from functools import reduce
from multiprocessing.dummy import Pool as ThreadPool 
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
    nbErr = 0
    pool = ThreadPool(4)
    result = []
    with open(argv[1], 'r') as file:
        result = pool.map(parse, file)
    print(reduce(lambda a,b: a + b, result),"syntax errors found")

if __name__ == '__main__':
    start = time.time()
    main(sys.argv)
    end = time.time()
    print("Done in ", end - start, "seconds")