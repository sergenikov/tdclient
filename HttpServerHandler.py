from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import urllib.request
from webbrowser import open_new
import json

REDIRECT_URL = 'http://localhost:8080/'
PORT = 8080

def get_access_token_from_url(url, payload):
    print("\nget_access_token_from_url: url=" + url)
    print("payload " + str(payload))

    data = urllib.parse.urlencode(payload)
    print("data " + str(data))
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(str(the_page.decode('ascii')))
    parsed_page = json.loads(str(the_page.decode('ascii')))
    print("access token=" + parsed_page['access_token'])
    return parsed_page['access_token']

class HTTPServerHandler(BaseHTTPRequestHandler):
    """
    HTTP Server callbacks to handle Todoist OAuth redirects
    """
    def __init__(self, request, address, server, a_id, a_secret):
        self.app_id = a_id
        self.app_secret = a_secret
        super().__init__(request, address, server)

    def do_GET(self):
        print("***** runnning do_GET")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if 'code' in self.path:
            self.auth_code = self.path.split('=')[2]
            print("*** auth_code=" + self.auth_code)

            url = 'https://todoist.com/oauth/access_token'
            payload = {
                'client_id'     : self.app_id,
                'client_secret' : self.app_secret,
                'code'          : self.auth_code,
                'redirect_uri'  : REDIRECT_URL }

            self.wfile.write(bytes('<html><h1>You may now close this window.'
                              + '</h1></html>', 'utf-8'))

            print("do_GET: before get_access_token_from_url")
            temp_token = get_access_token_from_url(url, payload)
            print("do_GET: access token=" + temp_token)
            self.server.access_token = temp_token

class TokenHandler:
    def __init__(self, a_id, a_secret):
        self._id = a_id
        self._secret = a_secret

    def get_access_token(self):

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
                    request, address, server, self._id, self._secret))
        #This function will block until it receives a request
        print("before handling request")
        httpServer.handle_request()
        #Return the access token
        print("get_access_token: access token " + httpServer.access_token)
        return httpServer.access_token
