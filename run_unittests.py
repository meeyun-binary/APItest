import os
import sys
import unittest


sys.path.append(os.path.join(sys.path[0],'..'))
test_dir = os.path.join(sys.path[0])
suite = unittest.TestLoader().discover(start_dir=test_dir,pattern='TestBuy.py')
#unittest.TextTestRunner(verbosity=1).run(suite)

ret = unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful()

if ret is True:
    sys.exit(0)

else:
    sys.exit(1)


