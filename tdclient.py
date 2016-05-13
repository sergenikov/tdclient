import sys, getopt
from APILink import APILink

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

    api_link = APILink()
    api_link.get_auth_token()

# run
if __name__ == "__main__":
    main(sys.argv[1:])
