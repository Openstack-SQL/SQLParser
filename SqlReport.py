class SqlReport:

    def __init__(self, nb_join = 0, nb_transac = 0):
        self.nb_join = nb_join
        self.nb_transac = nb_transac

    def mergeReport(self, report):
        self.nb_join = report.nb_join
        self.nb_transac = report.nb_transac
