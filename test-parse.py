import unittest, os, json
from parser import Parser
# TODO remove pprint in the long run
from pprint import pprint

class ParseTest(unittest.TestCase):

    parser = None
    response = None
    resp_file = None

    def setUp(self):
        print("\nsetUp: preparing tests")
        self.resp_file= open("resp.json", "r")
        self.response = json.load(self.resp_file)
        # pprint(self.response)
        self.parser = Parser(self.response)

    def tearDown(self):
        print("\ntearDown: closing response.json file")
        self.resp_file.close()

    """ Test methods """
    #def test_read_all_items(self):
    #    items = self.parser.get_today_tasks()
    #    if items is not None:
    #        self.assertEqual(7, len(items))

    def test_today_items(self):
        today_items = self.parser.get_today_tasks()
        print("due today list has %d items" % len(today_items))
        for item in today_items:
            print("due today: " + item['content'])



if __name__ == '__main__':
    unittest.main()
