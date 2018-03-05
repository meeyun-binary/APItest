import os
import sys
import unittest


sys.path.append(os.path.join(sys.path[0],'..'))
test_dir = os.path.join(sys.path[0])
suite = unittest.TestLoader().discover(start_dir=test_dir,pattern='Test*.py')
#unittest.TextTestRunner(verbosity=1).run(suite)

ret = unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful()

# ret is True(1) when test passes. 
# so change exit code to 0 when test passes
# thus, travis build will indicate build pass with exit code 0
if ret is True:
    sys.exit(0)

# travis build will should show fail when exit code is non-zero
else:
    sys.exit(1)


