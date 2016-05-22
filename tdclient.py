import Pyro4
import Pyro4.util
import sys

class TDClient(object):
    def print_projects(self, tdd):
        print("TDClient: getting list of projects")
        tdd.print_existing_projects()



sys.excepthook = Pyro4.util.excepthook

tdd = Pyro4.Proxy("PYRONAME:tdd.tdclient")
tdclient = TDClient()
tdclient.print_projects(tdd)
