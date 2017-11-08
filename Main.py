import sys
from SQLParser.SqlReport import SqlReport
from SQLParser.SqlReportProcessor import SqlReportProcessor

if __name__ == '__main__':
    reporter = SqlReportProcessor()
    report = reporter.reportFromFile(sys.argv[1])

    print(report.generalReport)
