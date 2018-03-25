# If there is no argument given, by default, it will use production server and production token
# To run in production: python run_unittests.py
# To run in QA: python run_unittests.py -s "www.binaryqa27.com" -a 1003 -t "lmmtw76c5gGAwvq"

# Currently travis.yml is set to production (python run_unittests.py)
# we need to manually change it if need the test run in QA


import argparse

parser = argparse.ArgumentParser()

# QA
parser.add_argument('-s', action='store',
                    dest='server',
                    help="Testing server. E.g. 'www.binaryqa20.com'",
                    default = "ws.binaryws.com")
# App ID
parser.add_argument('-a', action='store',
                    dest='app_id',
                    help="App ID. E.g. 1003",
                    default = 1089)
# Token
parser.add_argument('-t', action='store',
                    dest='token',
                    help="App token E.g. 'ei5EBsqQan230MG'",
                    default = "ei5EBsqQan230MG")

args = parser.parse_args()

