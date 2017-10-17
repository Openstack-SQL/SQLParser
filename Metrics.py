from SqlListener import SqlListener

class Metrics(SqlListener):
    nb_join = 0
    nb_transac = 0

    def enterJoin_operator(self, ctx):
        self.nb_join += 1

    def enterBegin_stmt(self, ctx):
        self.nb_transac += 1

    def howManyJoins(self):
        return self.nb_join

    def howManyTransactions(self):
        return self.nb_transac