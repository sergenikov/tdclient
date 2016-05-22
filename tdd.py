import Pyro4
import os, datetime

class TDDaemon(object):

    _api_link = None
    response = None
    today = None

    def __init__(self, api_link):
        self._api_link = api_link
        self.today = datetime.datetime.utcnow()
        print("Initializing TDDaemon; time today " + self.today)

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
        items = self.response['Items']
        for item in items:
            if item['due_date_utc'] == self.today:
                print(item['content'])
