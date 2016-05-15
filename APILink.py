import todoist, requests

CLIENT_ID = "4a393dd72f3d4abebb2e88adc8cd2518"
CLIENT_SECRET = "91af3f95d59d40fab7cd5aff6a57c6df"

class APILink(object):

    # Private
    _user = ""
    _api = ""

    def __init__(self):
        print("Creating APILink class")

    """
    Sync with TD server and return response of the API request.
    TODO: don't use this in the long run. It will be deprecated.
    """
    def syncronize(self, token):
        self._api = todoist.TodoistAPI(token)
        response = self._api.sync(resource_types=['all'])
        return response

    """
    Syncs and gets list of current projects
    """
    def get_project_list(self, api):
        response = api.sync(resource_types=['all'])
        for project in response['Projects']:
            print(project['name'])

    """
    Not used for anything right now. Stub for future OAuth2 stuff.
    """
    def get_auth_token(self):
        payload = {
            "client_id" : CLIENT_ID,
            "scope"     : "data:read",
            "state"     : CLIENT_SECRET
        }
        response = requests.get("https://todoist.com/oauth/authorize",
            params=payload)
        print()
        print(response.ok)
        print(response.content)
        print(response.url)
        print(response.is_redirect)

    def addItem(self, item_name):
        self._api.items.add(item_name)
