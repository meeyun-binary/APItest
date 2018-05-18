# If there is no argument given, by default, it will use production server and production token
# To run in production: python run_unittests.py
# To run in QA: python run_unittests.py -s "XXXX" -a XXXX -t "XXXX"

# Currently travis.yml is set to production (python run_unittests.py)
# we need to manually change it if need the test run in QA


import argparse

parser = argparse.ArgumentParser()

# QA
parser.add_argument('-s', action='store',
                    dest='server',
                    help="Testing server. E.g. 'XXXX'",
                    default = "XXXX")
# App ID
parser.add_argument('-a', action='store',
                    dest='app_id',
                    help="App ID. E.g. XXXX",
                    default = XXXX)
# Token
parser.add_argument('-t', action='store',
                    dest='token',
                    help="App token E.g. 'XXXX'",
                    default = "XXXX")

args = parser.parse_args()

