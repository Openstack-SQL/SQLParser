import sys
from SQLParser.SqlReport import SqlReport
from antlr4 import *
from SQLParser.parser.SqlLexer import SqlLexer
from SQLParser.parser.SqlParser import SqlParser
from SQLParser.parser.SqlListener import SqlListener
from SQLParser.Metrics import Metrics

class SqlReportProcessor:
    def __init__(self):
        generalReport = SqlReport()

    def reportFromFile(self, path):
        with open(path, 'r') as file:
            self.reportFromArray(file)

    def reportFromArray(self, requests):
        report = SqlReport()

        for request in requests:
            report.mergeReport(self.report(request))
        
        return report


    def report(self, request):
        report = SqlReport()

        tree = SqlParser(CommonTokenStream(SqlLexer(InputStream(request)))).sql_stmt()
        walker = ParseTreeWalker()
        metrics = Metrics()
        walker.walk(metrics, tree)

        report.nb_join += metrics.howManyJoins()
        report.nb_transac += metrics.howManyTransactions()
        self.generalReport.mergeReport(report)
        return report

