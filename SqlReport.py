import sys
from antlr4 import *
from SQLParser.parser.SqlLexer import SqlLexer
from SQLParser.parser.SqlParser import SqlParser
from SQLParser.parser.SqlListener import SqlListener
from SQLParser.Metrics import Metrics

class SqlReport:

    def reportFromFile(self, path):
        with open(path, 'r') as file:
            self.report(file)

    def report(self, requests):
        nb_join = 0
        nb_transac = 0

        for request in requests:
            tree = SqlParser(CommonTokenStream(SqlLexer(InputStream(request)))).sql_stmt()
            walker = ParseTreeWalker()
            metrics = Metrics()
            walker.walk(metrics, tree)

            nb_join += metrics.howManyJoins()
            nb_transac += metrics.howManyTransactions()

        print("Overall, there are")
        print(" -", nb_join, "joins")
        print(" -", nb_transac, "transactions")