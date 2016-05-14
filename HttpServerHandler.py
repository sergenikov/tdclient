from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen, HTTPError
from webbrowser import open_new

REDIRECT_URL = 'http://localhost:8080/'

PORT = 8080

def get_access_token_from_url(url):
    """
    Parse the access token from Facebook's response
    Args:
        uri: the facebook graph api oauth URI containing valid client_id,
             redirect_uri, client_secret, and auth_code arguements
    Returns:
        a string containing the access key
    """
    token = str(urlopen(url).read(), 'utf-8')
    return token.split('=')[1].split('&')[0]

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
        GRAPH_API_AUTH_URI = ('https://todoist.com/oauth/'
            + 'access_token?client_id=' + self.app_id + '&redirect_uri='
            + REDIRECT_URL + '&client_secret=' + self.app_secret + '&code=')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # TODO: modify this for the todoist code parsing
        if 'code' in self.path:
            self.auth_code = self.path.split('=')[1]
            self.wfile.write(bytes('<html><h1>You may now close this window.'
                              + '</h1></html>', 'utf-8'))
            self.server.access_token = get_access_token_from_url(
                    GRAPH_API_AUTH_URI + self.auth_code)
            print("\n*** ACCESS CODE START***")
            print(GRAPH_API_AUTH_URI + self.auth_code)
            print("*** ACCESS CODE END***\n")

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
                lambda request, address, server: HTTPServerHandler(
                    request, address, server, self._id, self._secret))
        #This function will block until it receives a request
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
