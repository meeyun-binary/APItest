import json
import unittest
import test_utils as tu
import time


class TestxServerTime(unittest.TestCase):

    def setUp(self):
        tu.log_out()

    def tearDown(self):
        return

    def test_server_time(self):
        input = json.dumps({
            "time": 1
        })

        server_time_response = tu.send_and_receive_ws_x_authorize(input)

        epoch_time = server_time_response["time"]
        current_time = int(time.time())

        self.assertAlmostEqual(epoch_time, current_time, delta=2)
        self.assertTrue('error' not in server_time_response)
