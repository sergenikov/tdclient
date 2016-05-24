import datetime

class Parser(object):

    response = None

    def __init__(self, response):
        self.response = response

    def get_today_tasks(self):
        items = self.response['Items']
        # print(items)
        return items


