import datetime
from pprint import pprint

class Parser(object):

    response = None

    def __init__(self, response):
        self.response = response

    def get_all_tasks(self):
        items = self.response['Items']
        # print(items)
        return items

    def get_today_tasks(self):
        items = self.response['Items']
        date = "Sun 22 May 2016 06:59:59"
        d = datetime.datetime.strptime(date, "%a %d %B %Y %H:%M:%S")
        for item in items:
            print("date: " + item['due_date'])
        return items
