import os
import sys
import unittest



sys.path.append(os.path.join(sys.path[0],'..'))
test_dir = os.path.join(sys.path[0])
suite = unittest.TestLoader().discover(start_dir=test_dir,pattern='Testx*.py')

ret = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()

# ret is True(1) when test passes. 
# so change exit code to 0 when test passes
# thus, travis build will indicate build pass with exit code 0
if ret is True:
    sys.exit(0)

# travis build will show fail when exit code is non-zero
else:
    sys.exit(1)


