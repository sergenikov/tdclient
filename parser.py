import datetime
from pprint import pprint

DATE_PATTERN = "%a %d %B %Y %H:%M:%S %z"

class Parser(object):

    response = None
    datetime_today = datetime.datetime.utcnow()

    def __init__(self, response):
        self.response = response

    def get_all_tasks(self):
        items = self.response['Items']
        return items

    def get_today_tasks(self):
        items = self.response['Items']
        due_today = []
        #date = "Sun 22 May 2016 06:59:59 +0000"
        for item in items:
            if item['due_date'] != "None" and item['due_date'] is not None:
                d = datetime.datetime.strptime(item['due_date'], DATE_PATTERN)
                if d.date() == self.datetime_today.date():
                    due_today.append(item)

        return due_today

    # Small helper to prints dates as strings
    def print_date(self, date):
        print("d.date(): " + date.date().strftime("%d %B %Y"))
