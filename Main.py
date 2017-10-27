import sys
from SqlReport import SqlReport

if __name__ == '__main__':
    # main(sys.argv)
    reporter = SqlReport()
    reporter.reportFromFile(sys.argv[1])