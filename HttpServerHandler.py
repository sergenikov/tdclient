from http.server import BaseHTTPRequestHandler, HTTPServer
# from urllib.request import urlopen, HTTPError
import urllib.parse
import urllib.request
from webbrowser import open_new
import json

REDIRECT_URL = 'http://localhost:8080/'

PORT = 8080

# def get_access_token_from_url(url, payload):
#     """
#     Parse the access token from Facebook's response
#     Args:
#         uri: the facebook graph api oauth URI containing valid client_id,
#              redirect_uri, client_secret, and auth_code arguements
#     Returns:
#         a string containing the access key
#     """
#     print("get_access_token_from_url: url=" + url)
#     # token_json = str(urlopen(url, data="").read())
#     token_json = str(urlopen(url))
#     # parsed_json = json.loads(token_json.read())
#     parsed_json = json.loads(token_json.read())
#     print("---------------------- access token=" + parsed_json['access_token'])
#     return parsed_json['access_token']

def get_access_token_from_url(url, payload):
    print("\nget_access_token_from_url: url=" + url)
    print("payload " + str(payload))

    data = urllib.parse.urlencode(payload)
    print("data " + str(data))
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(str(the_page.decode('ascii')))
    parsed_page = json.loads(str(the_page.decode('ascii')))
    print("access token=" + parsed_page['access_token'])
    return parsed_page['access_token']

class HTTPServerHandler(BaseHTTPRequestHandler):
    """
    HTTP Server callbacks to handle Facebook OAuth redirects
    """
    def __init__(self, request, address, server, a_id, a_secret):
        print("*** init server")
        self.app_id = a_id
        self.app_secret = a_secret
        super().__init__(request, address, server)

    def do_GET(self):
        print("***** runnning do_GET")
        # GRAPH_API_AUTH_URI = ('https://todoist.com/oauth/access_token'
        #     + '?client_id=' + self.app_id
        #     + '&redirect_uri='+ REDIRECT_URL
        #     + '&client_secret=' + self.app_secret
        #     + '&code=')


        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # TODO: modify this for the todoist code parsing
        if 'code' in self.path:
            self.auth_code = self.path.split('=')[2]
            print("*** auth_code=" + self.auth_code)

            TOKEN_EXCHANGE_URL = ('https://todoist.com/oauth/access_token'
                + '?client_id=' + self.app_id
                + '&client_secret=' + self.app_secret
                + '&code=' + self.auth_code
                + '&redirect_uri='+ REDIRECT_URL)

            url = 'https://todoist.com/oauth/access_token'

            payload = {
                'client_id'     : self.app_id,
                'client_secret' : self.app_secret,
                'code'          : self.auth_code,
                'redirect_uri'  : REDIRECT_URL }

            print(TOKEN_EXCHANGE_URL)

            self.wfile.write(bytes('<html><h1>You may now close this window.'
                              + '</h1></html>', 'utf-8'))

            print("do_GET: before get_access_token_from_url")
            temp_token = get_access_token_from_url(url, payload)
            print("do_GET: access token=" + temp_token)
            self.server.access_token = temp_token

class TokenHandler:
    """
    Class used to handle Facebook oAuth
    """
    def __init__(self, a_id, a_secret):
        self._id = a_id
        self._secret = a_secret

    def get_access_token(self):
        # ACCESS_URI = ('https://todoist.com/oauth/authorize'
        #     + '?client_id=' + self._id + '&redirect_uri='
        #     + REDIRECT_URL + "&scope=data:read")

        ACCESS_URI = ('https://todoist.com/oauth/authorize'
            + '?client_id=' + self._id
            + '&scope=data:read'
            + '&state=' + self._secret
            + '&redirect_uri=' + REDIRECT_URL)

        print("get_access_token: opening new window " + ACCESS_URI)
        open_new(ACCESS_URI)
        print("get_access_token: starting HTTP server on localhost:" + str(PORT))
        httpServer = HTTPServer(
                ('localhost', PORT),
                # this creates the RequestHandlerClass object within lambda function
                lambda request, address, server: HTTPServerHandler(
                    request, address, server, "4a393dd72f3d4abebb2e88adc8cd2518", "91af3f95d59d40fab7cd5aff6a57c6df"))
        # httpServer = HTTPServer(
        #         ('localhost', PORT),
        #         lambda request, address, server: HTTPServerHandler(
        #             request, address, server, self._id, self._secret))
        #This function will block until it receives a request
        print("before handling request")
        httpServer.handle_request()
        #Return the access token
        print("get_access_token: access token " + httpServer.access_token)
        return httpServer.access_token

# e226a4b146dc046ba0747be3f20163a6e11b7635

# $ curl "https://todoist.com/oauth/access_token" \
#     -d "client_id=0123456789abcdef" \
#     -d "client_secret=secret" \
#     -d "code=abcdef" \
#     -d "redirect_uri=https://example.com"