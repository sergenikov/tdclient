import Pyro4
import Pyro4.util
import sys

class TDClient(object):
    def get_all(self, tdd):
        print("TDClient: getting all items")
        tdd.print_existing_projects()

    def get_today(self, tdd):
        print("TDClient: getting today tasks")
        tdd.get_today_tasks()



sys.excepthook = Pyro4.util.excepthook

tdd = Pyro4.Proxy("PYRONAME:tdd.tdclient")
tdclient = TDClient()
# tdclient.get_all(tdd)
tdclient.get_today(tdd)
