import todoist, requests

CLIENT_ID = "4a393dd72f3d4abebb2e88adc8cd2518"
CLIENT_SECRET = "91af3f95d59d40fab7cd5aff6a57c6df"

class APILink(object):
    def __init__(self):
        print("Creating APILink class")

    def get_auth_token(self):
        payload = {
            "client_id" : CLIENT_ID,
            "scope"     : "data:read",
            "state"     : CLIENT_SECRET
        }
        r = requests.get("https://todoist.com/oauth/authorize", params=payload)
        print(r.text)
        print(r.url)

    def get_project_list(self):
        api = todoist.TodoistAPI()
        user = api.login('sergescr@live.ca', 'sovhozbushuiha')
        print(user['full_name'])
        response = api.sync(resource_types=['all'])
        for project in response['Projects']:
            print(project['name'])
