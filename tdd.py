import Pyro4
import os

class TDDaemon(object):

    _api_link = None

    def __init__(self, api_link):
        print("Initializing TDDaemon")
        self._api_link = api_link

    def print_existing_projects(self):
        response = self._api_link.syncronize(self._api_link.get_access_token())
        for project in response['Projects']:
            print(project['name'])

        user = response['user']
        command = "echo TDD contacted " + user['full_name'] + " " + user['email'] + "| wall"
        os.system(command)
