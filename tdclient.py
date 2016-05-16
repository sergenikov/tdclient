import sys, getopt, os, pwd
import HttpServerHandler
from APILink import APILink

usage = ("\nTODO usage")

def main(argv):
    """
    Main function
    """
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
    response = api_link.syncronize(api_link.get_access_token())
    for project in response['Projects']:
        print(project['name'])

    # 8310ec52fc38691d04d834ebe2025674fbb0c86b
    os._exit(0)

def read_app_info():
    """
    Reads client secret, client id and access token from $HOME/.todoist
    """
    home = os.path.expanduser("~")
    target = open(home + "/.todoist", 'r+')

    try:
        client_id = target.readline().rstrip().split(" ", 1)[1]
        client_secret = target.readline().rstrip().split(" ", 1)[1]

    except IndexError:
        print("read_app_info: no client id or client secret in ~/.todoist.")
    try:
        access_token = target.readline().rstrip().split(" ", 1)[1]
    except IndexError:
        print("read_app_info: no access token. Getting token.")
        access_token = get_oauth_access_token_with(client_id, client_secret)
        target.close()
        with open(home + "/.todoist", 'a') as target:
            target.write("access_token: " + access_token + "\n")

    print("client_id=\t" + client_id
            + "\nclient_secret=\t" + client_secret
            + "\naccess_token=\t" + access_token)

    return APILink(client_id, client_secret, access_token)

def get_oauth_access_token_with(client_id, client_secret):
    """
    Get access token if there is none in the config file.
    """
    tdAuth = HttpServerHandler.TokenHandler(client_id, client_secret)
    access_token = tdAuth.get_access_token()
    print("get_oauth_access_token_with: new access token " + access_token)
    return access_token

""" ************************** RUN ***************************** """
if __name__ == "__main__":
    main(sys.argv[1:])
