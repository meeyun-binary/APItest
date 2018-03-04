import os
import sys
import unittest


sys.path.append(os.path.join(sys.path[0],'..'))
# sys.path.append(os.path.join(sys.path[0],'testcases'))
# test_dir = os.path.join(sys.path[0],'testcases')
test_dir = os.path.join(sys.path[0])
suite = unittest.TestLoader().discover(start_dir=test_dir,pattern='TestBuy.py')
unittest.TextTestRunner(verbosity=1).run(suite)


