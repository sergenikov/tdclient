import Pyro4
import os
from parser import Parser
from pprint import pprint
import datetime

class TDDaemon(object):

    _api_link = None
    response = None
    today = None
    parser = None

    def __init__(self, api_link):
        self._api_link = api_link
        self.today = datetime.datetime.utcnow()
        self.parser = None
        print("Initializing TDDaemon")

    def print_existing_projects(self):
        response = self._api_link.syncronize(self._api_link.get_access_token())
        for project in response['Projects']:
            print(project['name'])

        # os.system("echo Printing from TDD | wall")

    def get_all(self):
        self.response = self._api_link.syncronize(self._api_link.get_access_token())
        get_today_tasks()

    def get_today_tasks(self):
        self.response = self._api_link.syncronize(self._api_link.get_access_token())
        self.parser = Parser(self.response)
        today_tasks = self.parser.get_today_tasks()
        for item in today_tasks:
            pprint(item)
