import sys, getopt, os, pwd
from APILink import APILink
# from HTTPServerHandler import HTTPServerHandler
# from HTTPServerHandler import TokenHandler
import HttpServerHandler

usage = ("\nTODO usage")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht")
        if len(argv) == 0:
            print(usage)
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == ("-h"):
            print(usage)
            sys.exit()

        elif opt == ("-t"):
            print("Getting today tasks")

    api_link = read_app_info()

    # TODO this has to be only done once when I need to login and auth this app
    # Once that's done, I only need to do this if token expired or was revoked.
    tdAuth = HttpServerHandler.TokenHandler(
        api_link.get_client_id(), api_link.get_client_secret())

    access_token = tdAuth.get_access_token()
    api_link.set_access_token(access_token)
    print("main: Access token " + api_link.get_access_token())

    response = api_link.syncronize(api_link.get_access_token())
    for project in response['Projects']:
        print(project['name'])
    # api_link.addItem("test new item")

"""
Reads app info such as client secret, client id and access token from
.todoist file in home directory.
"""
def read_app_info():
    home = os.path.expanduser("~")
    target = open(home + "/.todoist", 'r')
    client_id = target.readline().rstrip().split(" ", 1)[1]
    client_secret = target.readline().rstrip().split(" ", 1)[1]
    print("client_id=\t" + client_id + "\nclient_secret=\t" + client_secret)
    target.close()
    return APILink(client_id, client_secret)



""" ************************** RUN ***************************** """
if __name__ == "__main__":
    main(sys.argv[1:])
