import todoist, requests

class APILink(object):

    """ Private """
    _user = ""
    _api = ""
    _client_id = ""
    _client_secret = ""
    _access_token = ""

    def __init__(self, client_id, client_secret, access_token):
        """ Constructor """
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = access_token

    def get_client_id(self):
        return self._client_id

    def get_client_secret(self):
        return self._client_secret

    def set_access_token(self, token):
        self._access_token = token

    # @Property
    def get_access_token(self):
        return self._access_token

    def syncronize(self, token):
        """
        Sync with TD server and return response of the API request.
        """
        self._api = todoist.TodoistAPI(token)
        response = self._api.sync(resource_types=['all'])
        return response

    def get_project_list(self, api):
        """
        Syncs and gets list of current projects
        """
        response = api.sync(resource_types=['all'])
        for project in response['Projects']:
            print(project['name'])

    def get_auth_token(self):
        """
        Not used for anything right now. Stub for future OAuth2 stuff.
        """
        payload = {
            "client_id" : _client_id,
            "scope"     : "data:read",
            "state"     : _client_secret
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
