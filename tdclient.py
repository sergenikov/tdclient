import sys, getopt, os
from APILink import APILink
# from HTTPServerHandler import HTTPServerHandler
# from HTTPServerHandler import TokenHandler
import HttpServerHandler

usage = ("\nTODO usage")

CLIENT_ID = "4a393dd72f3d4abebb2e88adc8cd2518"
CLIENT_SECRET = "91af3f95d59d40fab7cd5aff6a57c6df"

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

    # api_link = APILink()
    # token = api_link.get_auth_token()
    # print(token)

    # fbAuth = HttpServerHandler.TokenHandler(os.environ['FB_APP_ID'],
                # os.environ['FB_APP_SECRET'])
    fbAuth = HttpServerHandler.TokenHandler(CLIENT_ID, CLIENT_SECRET)

    access_token = fbAuth.get_access_token()
    print("Access token " + access_token)


# run
if __name__ == "__main__":
    main(sys.argv[1:])
